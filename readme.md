# Nuevo sistema de comandos

## Descripción

Plugin creado para el sistema de [Generador de código SQL](https://github.com/maafinocode/fastapi-generator) que permite automatizar la creación de rutas y controladores mediante un código.

## Instalación
```
pip install generate-routers-fastapi-generator-jvngarcia==0.1.1
```

## Uso

```
makerouter
```

Luego pedirá el nombre de la ruta
```
Ingresa el nombre de la ruta: nombre_aqui
```

Se generará el código en:
````
app/routers/nombre_aqui.py
main.py -> Crea el include de FastAPI
imports_main.py -> Crea el import necesario

```
