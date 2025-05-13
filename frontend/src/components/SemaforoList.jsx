import { useEffect, useState } from "react";
import api from "../services/api"

function SemaforoList() {
    const [semaforos, setSemaforos] = useState([])

    useEffect(() => {
        api.get("/semaforos").then((res) => {
            console.log("Resposta da API: ", res.data)
            setSemaforos(res.data)
        })
            .catch((err) => {
            console.log("Erro ao buscar semáforos: ", err)
        })
    }, [])

    return (
        <div className="p-4">
            <h2 className="text-x1 font-bold mb-4">Semáforos</h2>
            <table className="w-full border">
                <thead>
                    <tr className="bg-gray-200">
                        <th className="p-2">ID</th>
                        <th className="p-2">Localização</th>
                        <th className="p-2">Status</th>
                        <th className="p-2">Luminosidade</th>
                    </tr>
                </thead>
                <tbody>
                    {semaforos.map((s) => (
                        <tr key={s.id} className="text-center border-t">
                            <td className="p-2">{s.id}</td>
                            <td className="p-2">{s.localizacao}</td>
                            <td className="p-2">{s.status_atual}</td>
                            <td className="p-2">{s.nivel_luminozidade}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default SemaforoList