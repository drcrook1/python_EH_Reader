import asyncio
import os

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    con_str = os.environ["CONN_STR"]
    eh_name = os.environ["EH_NAME"]
    print(con_str)
    print(eh_name)
    producer = EventHubProducerClient.from_connection_string(conn_str=con_str, eventhub_name=eh_name)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        while True:
            event_data_batch.add(EventData('First event'))
            event_data_batch.add(EventData('Second event'))
            event_data_batch.add(EventData('Third event'))

            # Send the batch of events to the event hub.
            await producer.send_batch(event_data_batch)
            print("waiting")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(run())