String Speed;
char LorR;
int i, s;

byte DataToRead[6];

void setup()
{
	// put your setup code here, to run once:
	Serial.begin(9600);
}

void loop()
{
	DataToRead[5] = '\n';
	Serial.readBytesUntil(char(13), DataToRead, 5);

	/* For Debugging, send string to RPi */
	for (i = 0; i < 6; i++)
	{
		Serial.write(DataToRead[i]);
		if (DataToRead[i] == '\n')
			break;
	}
	/* End of Debugging */

	LorR = DataToRead[0];
	Speed = "";
	for (i = 1; (DataToRead[i] != '\n') && (i < 6); i++)
	{
		Speed += DataToRead[i];
	}
	s = Speed.toInt();
	if (LorR == 'L')
	{
		// Turn left wheel with speed s
	}
	else if (LorR == 'R')
	{
		// Turn right wheel with speed s
	}
	delay(2000);
}
