# Calculadora: pruebas y calidad

## Instalacion y pruebas

```bash
python -m pip install -r requirements.txt
pytest
```

Las cuatro pruebas unitarias cubren suma, resta, multiplicacion y division.

## Cobertura

```bash
pytest --cov=calculadora --cov-report=term-missing --cov-report=html --cov-report=xml
```

Resultado obtenido: **100%** de cobertura de lineas (8 de 8; 0 sin probar). El reporte HTML queda en `htmlcov/index.html` y el XML en `coverage.xml`.

Una cobertura del 100% no garantiza que el programa este libre de errores: solo indica que las lineas fueron ejecutadas. No demuestra que todos los casos limite esten probados ni que los resultados sean correctos para todos los datos posibles.

## Revision manual de calidad

Ejemplo con problemas:

```python
def calcular_total(p, c):
	x = p * c
	return x
```

`p`, `c` y `x` no explican su significado; falta documentacion y la variable temporal es innecesaria. Esto puede señalar un Code Smell de legibilidad/mantenibilidad.

Version propuesta:

```python
def calcular_total(precio_unitario, cantidad):
	"""Calcula el importe antes de impuestos."""
	return precio_unitario * cantidad
```

## SonarQube Cloud

1. Importa este repositorio desde SonarQube Cloud y crea el proyecto.
2. Copia la clave de organizacion que muestra SonarCloud en `sonar-project.properties`, sustituyendo `TU_ORGANIZACION`. Confirma que `sonar.projectKey` coincide con la clave del proyecto.
3. Genera `coverage.xml` con el comando de cobertura anterior.
4. Ejecuta el análisis usando el método de CI recomendado por SonarCloud para el repositorio, con `SONAR_TOKEN` configurado como secreto. No guardes el token en el repositorio.
5. Revisa Code Smells, Bugs, Vulnerabilities y Coverage en el panel del proyecto.

El panel y sus hallazgos requieren una cuenta/proyecto de SonarQube Cloud y no se pueden generar desde este entorno sin esos permisos. No se incluye una captura ficticia; tras ejecutar el análisis, guarda una captura del panel como evidencia.