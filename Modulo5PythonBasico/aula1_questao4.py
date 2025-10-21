from datetime import datetime
# Exibe data e hora atuais no formato:
# Data: DD/MM/YYYY
# 
# Hora: HH:MM


def main():
    now = datetime.now()
    data = f"{now.day:02d}/{now.month:02d}/{now.year}"
    hora = f"{now.hour:02d}:{now.minute:02d}"
    print(f"Data: {data}\n")
    print(f"Hora: {hora}")

if __name__ == "__main__":
    main()