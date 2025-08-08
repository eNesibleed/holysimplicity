import { useState } from 'react';
import axios from 'axios';

export default function LoginPage({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/token/', {
        username,
        password,
      });
      localStorage.setItem('token', response.data.access);
      onLogin();
    } catch (err) {
      alert('Chyba při přihlášení');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Přihlášení</h2>
      <input
        type="text"
        placeholder="Uživatelské jméno"
        value={username}
        onChange={e => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Heslo"
        value={password}
        onChange={e => setPassword(e.target.value)}
        required
      />
      <button type="submit">Přihlásit</button>
    </form>
  );
}
