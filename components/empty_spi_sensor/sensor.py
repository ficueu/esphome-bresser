import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import ICON_EMPTY, UNIT_EMPTY


empty_spi_sensor_ns = cg.esphome_ns.namespace("empty_spi_sensor")
EmptySPISensor = empty_spi_sensor_ns.class_(
    "EmptySPISensor", cg.PollingComponent,
)

CONF_SENSOR1 = "temperature_sensor"
CONF_SENSOR2 = "humidity_sensor"


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(EmptySPISensor),
        cv.Optional(CONF_SENSOR1): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY, icon=ICON_EMPTY, accuracy_decimals=1
        ),
        cv.Optional(CONF_SENSOR2): sensor.sensor_schema(
            unit_of_measurement=UNIT_EMPTY, icon=ICON_EMPTY, accuracy_decimals=1
        ),
    }
).extend(cv.polling_component_schema("60s"))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if sensor_1_config := config.get(CONF_SENSOR1):
        sens = await sensor.new_sensor(sensor_1_config)
        cg.add(var.set_sensor1(sens))

    if sensor_2_config := config.get(CONF_SENSOR2):
        sens = await sensor.new_sensor(sensor_2_config)
        cg.add(var.set_sensor2(sens))

    if sensor_3_config := config.get(CONF_SENSOR3):
        sens = await sensor.new_sensor(sensor_3_config)
        cg.add(var.set_sensor3(sens))