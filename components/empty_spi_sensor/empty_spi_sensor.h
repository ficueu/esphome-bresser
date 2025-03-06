#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome
{
  namespace empty_spi_sensor
  {
    class EmptySPISensor : public sensor::Sensor,
                           public PollingComponent
    {
    public:
      void set_temperature_sensor(sensor::Sensor *temperature_sensor) { temperature_sensor_ = temperature_sensor; }
      void set_humidity_sensor(sensor::Sensor *humidity_sensor) { humidity_sensor_ = humidity_sensor; }
      
      void setup() override;
      void update() override;
      void loop() override;
      void dump_config() override;
    };

  } // namespace empty_spi_sensor
} // namespace esphome