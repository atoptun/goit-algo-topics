import asyncio
import random


class ServiceRequest:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.time: float = random.randrange(5, 25) / 10


ServiceQueue = asyncio.Queue[ServiceRequest | None]


class ServiceCenter:
    def __init__(self) -> None:
        self.queue: ServiceQueue = ServiceQueue(100)
        self.__last_id: int = 0

    def _generate_id(self) -> int:
        self.__last_id += 1
        return self.__last_id


    async def generate_request(self, name: str):
        new_request = ServiceRequest(self._generate_id())
        await self.queue.put(new_request)
        print(f'{name} added request (queue size: {self.queue.qsize()})')


    async def process_request(self, worker: str):
        request = await self.queue.get()
        try:
            if request is None:
                return False
            print(f'{worker} processes request "{request.id}", time {request.time:2f} sec')
            await asyncio.sleep(request.time)
        finally:
            self.queue.task_done()
            if request is not None:
                print(f'{worker} done request "{request.id}"')
        return True

    async def finish_work(self, count):
        print(f'Wait {self.queue.qsize()} requests ...')
        for _ in range(count):
            await self.queue.put(None)
        await self.queue.join()



async def customer(center: ServiceCenter, name: str):
    try:
        while True:
            await asyncio.sleep(random.randrange(5, 10) / 10)
            await center.generate_request(name)
    except asyncio.CancelledError:
        print("Customer stopped.")
        raise


async def worker(center: ServiceCenter, name: str):
    print(f"{name} started.")
    while True:
        try:
            cont = await center.process_request(name)
            if not cont:
                break
        except asyncio.CancelledError:
            print("CancelledError")
    print(f"{name} stopped.")


async def main():
    center = ServiceCenter()

    clients = [asyncio.create_task(customer(center, f"Customer-{i}")) for i in range(2)]
    workers = [asyncio.create_task(worker(center, f"Worker-{i}")) for i in range(2)]

    print("Service center opened ...")
    try:
        await asyncio.gather(*clients, *workers)
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("Service center finishing work ...")
        for c in clients:
            c.cancel()
        await asyncio.gather(*clients, return_exceptions=True)

    await center.finish_work(len(workers))

    await asyncio.gather(*workers, return_exceptions=True)

    print("Service center work done")


if __name__ == '__main__':
    asyncio.run(main())

