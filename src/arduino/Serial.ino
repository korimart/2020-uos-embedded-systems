String Speed;
char LorR;
int i, s;

#define motorL_1 2
#define motorL_2 4
#define motorR_1 7
#define motorR_2 8
#define motorL_SpeedControler 9
#define motorR_SpeedControler 10
byte DataToRead[6];

void setup()
{
	// put your setup code here, to run once:
	Serial.begin(9600);
	pinMode(motorL_1, OUTPUT);
	pinMode(motorL_2, OUTPUT);
	pinMode(motorR_1, OUTPUT);
	pinMode(motorR_2, OUTPUT);
	pinMode(motorL_SpeedControler, OUTPUT);
	pinMode(motorR_SpeedControler, OUTPUT);
}

void loop()
{
	// 1-HIGH 2-LOW -> 앞으로가기
	digitalWrite(motorR_1, HIGH);
	digitalWrite(motorR_2, LOW);

	DataToRead[5] = '\n';
	Serial.readBytesUntil(char(13), DataToRead, 5);

	LorR = DataToRead[0];
	Speed = "";

	for (i = 1; (DataToRead[i] != '\n') && (i < 6); i++)
	{
		Speed += DataToRead[i];
	}

	s = Speed.toInt();

	if (LorR == 'L')
	{
		if (DataToRead[1] == '0')
		{
			digitalWrite(motorL_1, LOW);
			digitalWrite(motorL_2, LOW);
			analogWrite(motorL_SpeedControler, 0);
		}

		else if (DataToRead[1] == '1')
		{
			digitalWrite(motorL_1, HIGH);
			digitalWrite(motorL_2, LOW);
			analogWrite(motorL_SpeedControler, 70);
		}

		else
		{
			digitalWrite(motorL_1, HIGH);
			digitalWrite(motorL_2, LOW);
			analogWrite(motorL_SpeedControler, 80);
		}
	}
	if (LorR == 'R')
	{
		if (DataToRead[1] == '0')
		{
			digitalWrite(motorR_1, LOW);
			digitalWrite(motorR_2, LOW);
			analogWrite(motorR_SpeedControler, 0);
		}

		else if (DataToRead[1] == '1')
		{
			digitalWrite(motorR_1, HIGH);
			digitalWrite(motorR_2, LOW);
			analogWrite(motorR_SpeedControler, 70);
		}

		else
		{
			digitalWrite(motorR_1, HIGH);
			digitalWrite(motorR_2, LOW);
			analogWrite(motorR_SpeedControler, 80);
		}
	}
}