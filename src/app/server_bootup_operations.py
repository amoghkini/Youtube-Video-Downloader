from messaging_engine.producer import MessagingEngineProducer

def server_bootup_operations():
    pass
    

def declare_exchange():
    message = MessagingEngineProducer()
    message.declare_exchange()