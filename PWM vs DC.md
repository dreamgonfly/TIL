# PWM vs. DC

Fan control is the management of the rotational speed of an electric fan.

# Direct Current

DC changes fan speed by varying the applied voltage, but this number is constant (ie DC). So, maybe 5V corresponds to 1000 RPM, whereas 3V corresponds to 600 RPM.

For example, computer fans are typically 12v, so if you only send 7v to them instead, you get roughly 60% speed.

Control for these fans is less common as a built in feature in motherboards, but has been becoming increasingly standard over the past 5 years. Many standalone fan controllers that use knobs or sliders are also controlling things this way.

# Pulse Width Modulation

PWM (pulse width modulation) fans have an applied DC voltage, which stays constant (might be 0V, not sure), and varies the fan speed by modulating this DC voltage with pulses of varying (temporal) width. The pulses are 'digital' and are ideally modeled as step functions (rectangular). If the width and periodicity of pulses were the same, you would get a square wave voltage signal driving the fans. If you averaged over the amplitudes of these pulses over a period, you would recover the applied voltage from the DC method.

They always supply the full 12v, but also send a PWM signal, which basically turns the motor off and on extremely quickly. So to get 60% speed on this, you still send the full 12v, but the motor is only on 60% of the time.

# Compatibility

If you have a bunch of 4-pin connectors then you should get PWM fans. If you only have 3-pins, then you should get DC fans. Both will give you similar results.

You will not be able to enable PWM for DC fans. They will run as DC no matter what, since they only have 3-pin connectors. Enabling PWM for a DC fan might just make it run at 100% all the time (in this instance, its a good idea to disable PWM for the DC fans you have plugged in)

# Comparison

## Pin

- DC is 3-pin
- PWM is 4-pin

## Ability

PWM fans are typically capable of going to much lower minimum speeds compared to DC, they can typically dip down to 20% or lower. Whereas DC is typically in the 40-60% range for minimums.

DC aren't far behind anymore. There isn't much difference between them with modern boards.

## Price

DC fans are available because they are cheaper and pretty much just as effective.

# References

[What is the difference between DC and PWM fans, and which is better?](https://www.reddit.com/r/buildapc/comments/a1i7tp/what_is_the_difference_between_dc_and_pwm_fans/)

[Computer fan control](https://en.wikipedia.org/wiki/Computer_fan_control)

[Pulse-width modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation)

[쿨러잘알 없냐 dc모드랑 pwm모드 정확히 차이가 뭐야 - 컴퓨터 본체 갤러리](https://gall.dcinside.com/board/view/?id=pridepc_new3&no=7646458)