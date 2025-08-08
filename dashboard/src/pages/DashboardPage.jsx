import { useEffect, useState } from 'react';
import axios from 'axios';

export default function DashboardPage() {
  const [poptavky, setPoptavky] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
        const token = localStorage.getItem('token');
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/poptavky/poptavky/', {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
          console.log('ODPOVĚĎ Z API:', response.data); // <- přidat tento řádek
          setPoptavky(response.data);
        } catch (error) {
          console.error('Chyba při načítání dat:', error);
        }
      };      

    fetchData();
  }, []);

  return (
    <div>
      <h2>Seznam poptávek</h2>
      <ul>
        {poptavky.map(p => (
          <li key={p.id}>
            <strong>{p.email}</strong><br />
            {p.zprava}<br />
            <em>{p.datum}</em>
          </li>
        ))}
      </ul>
    </div>
  );
}
