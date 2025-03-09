# Telegram
It is using to send multiple messages to anyone.
`⚠️It is important to avoid sending more than 100 SMS using your main account.` If you send a potential threat to ban your Telegram account.

![Telegram logo](https://github.com/d3rkwind/Assets/blob/main/IMG_20250309_112244.jpg)


## Installing directly
You first need to clone or download the repository to your local directory, then move into the project directory as shown in the example, and then run the following command:
```bash
pkg install git -y
pkg install python -y
git clone https://github.com/d3rkwind/Telegram.git
```
## How to use ?
First, open the link https://my.telegram.org and log in. Afterwards, obtain your API id and API hash. Next, open the directory and run this program below this command:

```bash
cd Telegram
pip install -r requirements.txt
python telegram.py
```

## Fix problems 
When you manually stop the middle of the process by pressing **ctrl + z**, you can solve it with this command.

```bash
ps aux
```
```bash
kill -9 <PID>
```
Enter in <PID> the process ID of the programme telegram.py. When you enter first command then see the process ID of the programme after the username of terminal.
