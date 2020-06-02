
import os

import click
import toml

snap_userdata = os.environ['SNAP_USER_DATA']


@click.command()
@click.option('--mqtt-broker-ip', prompt='MQTT broker IP', help='MQTT broker IP', default='unbelievable-politician.cloudmqtt.com')
@click.option('--mqtt-broker-port', prompt='MQTT broker port', help='Mqtt broker port', default='8883')
@click.option('--ssl-cert-path', prompt='What is the path of the SSL certficate?', default='ca-certificates.crt')
@click.option('--mqtt-username', prompt='MQTT username', default='username')
def init(mqtt_broker_ip,
         mqtt_broker_port,
         ssl_cert_path,
         mqtt_username
         ):
    config = f"""

    title = "Building Python Snaps"

    [mqtt_connection]
    mqtt_broker_ip = '{mqtt_broker_ip}'
    mqtt_broker_port = '{mqtt_broker_port}'
    ssl_cert_path = '{ssl_cert_path}'
    mqtt_username = '{mqtt_username}'
    """
    parsed_config = toml.loads(config)
    formatted_config = toml.dumps(parsed_config)

    with open(snap_userdata + '/config.toml', 'w+') as f:
        f.write(formatted_config)
