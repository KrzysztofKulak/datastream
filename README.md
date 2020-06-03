# datastream

Datastream is a set of two apps and two importable modules.
Their collective goal is to achieve configurable data streaming between other Python apps or services. 

## dataproducer
`dataproducer` is a module that can be imported into an existing script, app, etc.. It contains a `enqueue_data` method, that takes json-formatted data and sends it to `dataqueue` app hosted on url specified by `DATAQUEUE_URL` environment variable (it is also required to provide the `dataqueue` as `DATAQUEUE_API_KEY` env variable).

## dataqueue
`dataqueue` is an app that intakes the data provided by dataproducers (apps, scripts, etc. using the `dataproducer` module) and assigns it to corresponding queues according to configured rules. The data stored on queues can be later read (dequeued) by `datamanager`.

## datamanager 
`datamanager` is an app that queries queues in the `dataqueue` app in intervals, can apply some data transformation to acquired data and sends the data to dataconsumers (apps or scripts using the `dataconsumer` module) according to configuration.

## dataconsumer
`dataconsumer` is a module that allow the app or script it is imported into to intake formatted data assigned to it by `datamanager` and do required work on that data (i.e. save it in data warehouse system or process it and add it to a data lake). 

