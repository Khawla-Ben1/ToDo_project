import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState({ title: '', description: '' });

    useEffect(() => {
        axios.get('/api/tasks/')
            .then(response => setTasks(response.data))
            .catch(error => console.error('Error fetching tasks:', error));
    }, []);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewTask(prevState => ({ ...prevState, [name]: value }));
    };

    const addTask = () => {
        axios.post('/api/tasks/', newTask)
            .then(response => setTasks([...tasks, response.data]))
            .catch(error => console.error('Error adding task:', error));
    };

    const deleteTask = (id) => {
        axios.delete(`/api/tasks/${id}/`)
            .then(() => setTasks(tasks.filter(task => task.id !== id)))
            .catch(error => console.error('Error deleting task:', error));
    };

    return (
        <div>
            <h1>To-Do List</h1>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        {task.title} - {task.description}
                        <button onClick={() => deleteTask(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
            <input
                type="text"
                name="title"
                placeholder="Task Title"
                value={newTask.title}
                onChange={handleInputChange}
            />
            <input
                type="text"
                name="description"
                placeholder="Task Description"
                value={newTask.description}
                onChange={handleInputChange}
            />
            <button onClick={addTask}>Add Task</button>
        </div>
    );
}

export default App;
