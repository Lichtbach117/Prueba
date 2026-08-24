from rich.console import Console
from rich.table import Table

console = Console()

tasks = [
    {"name": "Preparar informe", "completed": False},
    {"name": "Revisar código", "completed": True},
    {"name": "Actualizar documentación", "completed": False},
]


def show_tasks():
    table = Table(title="TaskFlow")
    table.add_column("ID", justify="right")
    table.add_column("Tarea")
    table.add_column("Estado")

    for index, task in enumerate(tasks, start=1):
        status = "Completada" if task["completed"] else "Pendiente"
        table.add_row(str(index), task["name"], status)

    console.print(table)


def add_task():
    name = input("Nombre de la tarea: ")
    tasks.append({"name": name, "completed": False})
    console.print("Tarea agregada.")


def complete_task():
    show_tasks()
    try:
        task_id = int(input("ID de la tarea completada: "))
        tasks[task_id - 1]["completed"] = True
        console.print("Tarea actualizada.")
    except (ValueError, IndexError):
        console.print("ID inválido.")

def prueba():
    print ("hola")


def main():
    while True:
        console.print("\n[bold]=== TASKFLOW ===[/bold]")
        console.print("1. Ver tareas")
        console.print("2. Agregar tarea")
        console.print("3. Marcar tarea como completada")
        console.print("4. Salir")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
            show_tasks()
        elif option == "2":
            add_task()
        elif option == "3":
            complete_task()
        elif option == "4":
            console.print("Hasta luego.")
            break
        else:
            console.print("Opción inválida.")


if __name__ == "__main__":
    main()

print("hola mundo1")