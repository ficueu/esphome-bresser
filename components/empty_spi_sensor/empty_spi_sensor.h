#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome
{
  namespace empty_spi_sensor
  {
    class EmptySPISensor : public sensor::Sensor,
                           public PollingComponent,
    {
    public:
      void setup() override;
      void update() override;
      void loop() override;
      void dump_config() override;
    };

  } // namespace empty_spi_sensor
} // namespace esphome