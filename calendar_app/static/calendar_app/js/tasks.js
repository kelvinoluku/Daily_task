// Function to render tasks from the database
function renderTasks(tasks) {
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = ""; // Clear existing tasks

    tasks.forEach((task) => {
        const taskItem = document.createElement("div");
        taskItem.classList.add("task-item");
        taskItem.innerHTML = `
            <h3>${task.name}</h3>
            <p>Due Date: ${task.due_date}</p>
            <button class="edit-task" data-id="${task.id}">Edit</button>
            <button class="delete-task" data-id="${task.id}">Delete</button>
        `;
        taskList.appendChild(taskItem);
    });
}

// Function to fetch tasks from your Django API
async function fetchTasks() {
    try {
        const response = await fetch("/api/tasks/"); // Replace with your API endpoint
        if (!response.ok) {
            throw new Error("Network response was not ok.");
        }
        const tasks = await response.json();
        renderTasks(tasks);
    } catch (error) {
        console.error("Error fetching tasks:", error);
    }
}

// Initial fetch and render tasks
fetchTasks();
