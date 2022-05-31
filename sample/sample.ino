float humidity;
float temperature_c;
float temperature_f;
float heat_index_c;
float heat_index_f;
float uv_index;
float uv_sensor_voltage;
float decimal_part;
float  gps_latitudes[5] = {18.514140068659295, 18.516583814083617, 18.519552804341547, 18.519632733862686, 18.516092783260714};
float  gps_longitudes[5] = {73.81542419460978, 73.81525560103589, 73.8149545363522, 73.81801340273735, 73.81767618704637};
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  for (int i = 0; i < 5; i++)
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

    Serial.print(random(3, 5) + decimal_part);
    Serial.print(",");

    Serial.print(gps_latitudes[i],14);
    Serial.print(",");

    Serial.println(gps_longitudes[i],14);

    //    Serial.println(decimal_part);
    delay(1000);
  }
}
