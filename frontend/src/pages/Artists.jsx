import { useEffect, useState } from "react";
import api from "../services/api";

function Artists() {
    const [artists, setArtists] = useState([]);
    const [showForm, setShowForm] = useState(false);
    const [editingId, setEditingId] = useState(null);

    const [newArtist, setNewArtist] = useState({
    name: "",
    specialization: "",
    experience: "",
    country: "",
});

    useEffect(() => {
        api.get("/artists")
            .then((response) => {
                setArtists(response.data);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    const addArtist = () => {

    api.post("/artists", newArtist)
        .then(() => {

            alert("Artist added successfully!");

            window.location.reload();

        })
        .catch((error) => {

            console.log(error);

            alert("Failed to add artist.");

        });

};
    const deleteArtist = (id) => {

    if (!window.confirm("Delete this artist?")) {
        return;
    }

    api.delete(`/artists/${id}`)
        .then(() => {

            alert("Artist deleted successfully!");

            window.location.reload();

        })
        .catch((error) => {

            console.log(error);

            alert("Failed to delete artist.");

        });

};

const editArtist = (artist) => {

    setEditingId(artist.artist_id);

    setNewArtist({
        name: artist.name,
        specialization: artist.specialization,
        experience: artist.experience,
        country: artist.country,
    });

    setShowForm(true);

};
    
    return (
        <div>

<div className="flex justify-between items-center mb-6">

    <h1 className="text-3xl font-bold">
        Artists
    </h1>

    <button
        onClick={() => setShowForm(!showForm)}
        className="bg-violet-400 hover:bg-violet-500 text-white px-5 py-2 rounded-lg"
    >
        + Add Artist
    </button>
{showForm && (
    <div className="bg-white p-6 rounded-lg shadow mb-6">

        <h2 className="text-xl font-semibold mb-4">
            Add Artist
        </h2>

        <input
            type="text"
            placeholder="Name"
            value={newArtist.name}
            onChange={(e) => setNewArtist({...newArtist, name: e.target.value})}
            className="border p-2 rounded w-full mb-3"
        />

        <input
            type="text"
            placeholder="Specialization"
            value={newArtist.specialization}
            onChange={(e) => setNewArtist({...newArtist, specialization: e.target.value})}
            className="border p-2 rounded w-full mb-3"
        />

        <input
            type="number"
            placeholder="Experience"
            value={newArtist.experience}
            onChange={(e) => setNewArtist({...newArtist, experience: e.target.value})}
            className="border p-2 rounded w-full mb-3"
        />

        <input
            type="text"
            placeholder="Country"
            value={newArtist.country}
            onChange={(e) => setNewArtist({...newArtist, country: e.target.value})}
            className="border p-2 rounded w-full mb-3"
        />

        <button 
        onClick={addArtist}
        className="bg-green-500 text-white px-4 py-2 rounded">
            Save Artist
        </button>

    </div>
)}
</div>
            <table className="w-full bg-white shadow rounded">

                <thead className="bg-pink-200 text-blue-950">

                    <tr>
                        <th className="p-3">ID</th>
                        <th className="p-3">Name</th>
                        <th className="p-3">Specialization</th>
                        <th className="p-3">Experience</th>
                        <th className="p-3">Country</th>
                        <th className="p-3">Actions</th>
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
                            <td className="p-3">
                                <button
                                    onClick={() => editArtist(artist)}
                                    className="bg-rose-300 hover:bg-purple-300 text-black px-3 py-1 rounded mr-2"
                                >
                                    Edit
                                </button>

                                <button
                                    onClick={() => deleteArtist(artist.artist_id)}
                                    className="bg-indigo-200 hover:bg-purple-300 text-black px-4 py-2 rounded"
                                >
                                    Delete
                                </button>
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>
    );
}

export default Artists;