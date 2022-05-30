float humidity;
float temperature_c;
float temperature_f;
float heat_index_c;
float heat_index_f;
float uv_index;
float uv_sensor_voltage;
float decimal_part;
void setup()
{
    Serial.begin(9600);
}

void loop()
{
    decimal_part = random(3) * 0.9;
    temperature_c = random(20, 40) + decimal_part;
    temperature_f = temperature_c * 1.8 + 32 + decimal_part;

    Serial.print(random(40, 60) + decimal_part);
    Serial.print(",");

    Serial.print(temperature_c);
    Serial.print(",");

    Serial.print(temperature_f);
    Serial.print(",");

    Serial.print(temperature_c - 2);
    Serial.print(",");

    Serial.print(temperature_f - 2);
    Serial.print(",");

    Serial.print(random(300, 400) + decimal_part);
    Serial.print(",");

    Serial.println(random(3, 5) + decimal_part);

    //    Serial.println(decimal_part);
    delay(1000);
}
