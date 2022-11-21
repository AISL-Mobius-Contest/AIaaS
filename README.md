# AIaaS
AIaaS is a service that users use when they want to make predictions through artificial intelligence models based on their own sensor values or data.

Using the oneM2M standard IoT platform, AIaaS was developed by linking the IoT hub responsible for connection with the physical world and the AI hub responsible for AI as a service.

Kafka was used as an AI as a Service broker to support high-speed interworking between IoT hub and AI hub.


# Installation Guide
1. git clone https://github.com/Blossom-Mobius-Contest/AIaaS.git

2. **Download the modules you need.**

3. The nCube-Thyme-Node.js was used to create a container and create a sub.

4. Run main.py on IoTHub_Mgmt,Kafka_Mgmt.

5. Run subscribe.py on AIHub_Mgmt.

6. **You need to set the file path or server ip and port related contents separately from the codes.**