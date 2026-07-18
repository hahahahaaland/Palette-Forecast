import { useEffect, useState } from "react";
import api from "../services/api";

function Artists() {
    const [artists, setArtists] = useState([]);

    useEffect(() => {
        api.get("/artists")
            .then((response) => {
                setArtists(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    return (
        <div>

            <h1 className="text-3xl font-bold mb-6">
                Artists
            </h1>

            <table className="w-full bg-white shadow rounded">

                <thead className="bg-pink-200 text-blue-950">

                    <tr>
                        <th className="p-3">ID</th>
                        <th className="p-3">Name</th>
                        <th className="p-3">Specialization</th>
                        <th className="p-3">Experience</th>
                        <th className="p-3">Country</th>
                    </tr>

                </thead>

                <tbody>

                    {artists.map((artist) => (

                        <tr
                            key={artist.artist_id}
                            className="border-b text-center"
                        >

                            <td className="p-3">{artist.artist_id}</td>
                            <td className="p-3">{artist.name}</td>
                            <td className="p-3">{artist.specialization}</td>
                            <td className="p-3">{artist.experience}</td>
                            <td className="p-3">{artist.country}</td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default Artists;