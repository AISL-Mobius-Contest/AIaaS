import paho.mqtt.client as mqtt
import kafka_module


def on_connect(client, userdata, flags, rc): # 클라이언트가 서버에게서 CONNACK 응답을 받을 때 호출되는 콜백
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg): # 서버에게서 PUBLISH 메시지를 받을 때 호출되는 콜백
    msg = msg.payload.decode("utf-8")
    msg = eval(msg)
    msg_type = msg["pc"]["m2m:sgn"]["nev"]["rep"]

    for key in msg_type.keys():
        if key == "m2m:cin":
            sensorData = msg_type["m2m:cin"]["con"]
            sensorData = str(sensorData)
            kafka_module.Producer(source_, sensorData)
            print(source_)
            print("**sensorData upload**")
        
        else:
            pass
                

def subscribing(source):
    # 새로운 클라이언트 생성
    global source_
    source_ = source
    
    client = mqtt.Client()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
    # on_message(발행된 메세지가 들어왔을 때)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    # address : Mobius Server IP, port: MQTT_PORT에 연결
    client.connect(' ', )
    # common topic 으로 메세지 발행 (건드리지 마세요)
    client.subscribe('/oneM2M/req/+/'+source+'/#')
    client.loop_forever() # 네트웍 트래픽을 처리, 콜백 디스패치, 재접속 등을 수행하는 블러킹 함수
                        # 멀티스레드 인터페이스나 수동 인터페이스를 위한 다른 loop*() 함수도 있음

