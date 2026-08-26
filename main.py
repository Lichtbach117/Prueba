from rich.console import Console
from rich.table import Table

console = Console()

tasks = [
    {"name": "Preparar informe", "completed": False, "priority": "Alta"},
    {"name": "Revisar código", "completed": True, "priority": "Media"},
    {"name": "Actualizar documentación", "completed": False, "priority": "Baja"},
]


def show_tasks():
    table = Table(title="TaskFlow")
    table.add_column("ID", justify="right")
    table.add_column("Tarea")
    table.add_column("Estado")
    table.add_column("Prioridad")

    for index, task in enumerate(tasks, start=1):
        status = "Completada" if task["completed"] else "Pendiente"
        table.add_row(str(index), task["name"], status, task["priority"])

    console.print(table)

def choose_priority():
    while True:
        print("INDIQUE LA PRIORIDAD DE LA TAREA")
        print ("1. Alta")
        print ("2. Media")
        print ("3. Baja")

        option = input("Selecciones una opcion:").strip()

        if option == "1":
            return "Alta"
        elif option == "2":
            return "Media"
        elif option == "3":
            return "Baja"
        else:
            print("Opción inválida.\n")


def add_task():
    name = input("Nombre de la tarea: ")
    print("Prioridad de la tarea: ")
    priority = choose_priority()
    tasks.append({"name": name, "completed": False, "priority": priority})
    console.print("Tarea agregada.")


def complete_task():
    show_tasks()
    try:
        task_id = int(input("ID de la tarea completada: "))
        tasks[task_id - 1]["completed"] = True
        console.print("Tarea actualizada.")
    except (ValueError, IndexError):
        console.print("ID inválido.")


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
