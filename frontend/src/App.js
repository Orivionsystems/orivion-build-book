import React, { useState, useEffect } from 'react';

function App() {
  const [tasks, setTasks] = useState([]);
  const [description, setDescription] = useState('');
  const [agent, setAgent] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/tasks/')
      .then((res) => res.json())
      .then((data) => setTasks(data))
      .catch((err) => console.error(err));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newTask = { description, assigned_agent: agent || null };
    await fetch('http://localhost:8000/tasks/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newTask),
    })
      .then((res) => res.json())
      .then((createdTask) => {
        setTasks([...tasks, createdTask]);
        setDescription('');
        setAgent('');
      })
      .catch((err) => console.error(err));
  };

  return (
    <div>
      <h1>ORIVION Dashboard</h1>
      <h2>Create Task</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Task description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
        <select value={agent} onChange={(e) => setAgent(e.target.value)}>
          <option value="">Select agent (optional)</option>
          <option value="CEOAgent">CEO Agent</option>
          <option value="ResearchAgent">Research Agent</option>
        </select>
        <button type="submit">Create</button>
      </form>

      <h2>Tasks</h2>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {task.description} — Assigned to: {task.assigned_agent || 'None'}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
