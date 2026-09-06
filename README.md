# Sistema de Gestión de Tienda - Táctica Vencer o Morir

## Información del proyecto

**Sistema:** Sistema de Gestión de la Tienda Táctica Vencer o Morir

**Módulo:** Gestión de Productos

**Tecnologías:** Python + Django

**Repositorio:** GitHub

## Descripción

El proyecto consiste en el desarrollo de un sistema de gestión para la tienda Táctica Vencer o Morir.

El módulo seleccionado para la implementación corresponde a la Gestión de Productos, cuyo objetivo es permitir administrar la información de los productos disponibles en la tienda.

## Módulo a implementar

### Gestión de Productos

El módulo permitirá gestionar la información relacionada con los productos de la tienda, incluyendo su registro, consulta, modificación y demás operaciones que sean definidas durante el desarrollo del proyecto.

## Flujo de trabajo con Git

Se utilizará un flujo de trabajo basado en GitHub Flow.

La rama `main` será la rama principal y deberá mantenerse estable.

Para desarrollar cada funcionalidad se creará una rama independiente utilizando la siguiente nomenclatura:

`feature/nombre-de-la-funcionalidad`

Para este proyecto se utilizará inicialmente:

`feature/gestion-productos`

Una vez finalizado el trabajo de la rama, se realizará un commit con un mensaje descriptivo y posteriormente se subirá la rama al repositorio remoto.

Finalmente, se creará un Pull Request para revisar y fusionar los cambios hacia la rama `main`.

## Integración continua

El proyecto utilizará GitHub Actions para ejecutar un pipeline de Integración Continua (CI).

El pipeline se ejecutará automáticamente cuando se realicen cambios mediante `push` o Pull Request.

En esta etapa el CI tendrá como objetivo verificar que el pipeline se ejecute correctamente. En las siguientes etapas se incorporarán las pruebas automatizadas del módulo.

## Estructura inicial

```text
gestion-tienda-tactica/
├── README.md
├── .gitignore
├── src/
└── .github/
    └── workflows/
        └── ci.yml