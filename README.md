# Calculadora Remota Pyro5

Comunicación cliente-servidor usando Pyro5 (Python Remote Objects) con interfaz web.

## Requisitos

- Python 3.7+
- Pyro5
- Flask

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### 1. Iniciar el Servidor

```bash
python servidor.py
```

### 2. Iniciar el Cliente Web

En otra terminal:

```bash
python cliente_web.py
```

La aplicación estará disponible en `http://localhost:5000`

## Operaciones Disponibles

- Suma
- Resta
- Multiplicación
- División

## Estructura

```
Pyro5/
├── servidor.py           # Servidor Pyro5
├── cliente_web.py        # Cliente Web Flask
├── requirements.txt      # Dependencias
├── templates/
│   └── index.html        # Interfaz web
└── static/               # Archivos estáticos
```

## Notas

- El servidor corre en puerto 9090
- La aplicación web corre en puerto 5000
- Para conectar desde otra máquina, cambia `localhost` por la IP del servidor
