import { useEffect, useState } from "react";
import api from "../services/api";

function Artworks() {

    const [artworks, setArtworks] = useState([]);
    const [showForm, setShowForm] = useState(false);
    const [editingId, setEditingId] = useState(null);

    const [newArtwork, setNewArtwork] = useState({
        title: "",
        artist_id: "",
        style_id: "",       
        medium_id: "",
        base_price: "",
        status: "Available",
    });

    useEffect(() => {

        api.get("/artworks")
            .then((response) => {
                setArtworks(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, []);

    const addArtwork = () => {

    if (editingId) {

        api.put(`/artworks/${editingId}`, newArtwork)
            .then(() => {

                alert("Artwork updated successfully!");

                window.location.reload();

            })
            .catch((error) => {

                console.error(error);

                alert("Failed to update artwork.");

            });

    } else {

        api.post("/artworks", newArtwork)
            .then(() => {

                alert("Artwork added successfully!");

                window.location.reload();

            })
            .catch((error) => {

                console.error(error);

                alert("Failed to add artwork.");

            });

    }

};

    const editArtwork = (artwork) => {

    console.log(artwork);

    setEditingId(artwork.artwork_id);

    setNewArtwork({
        title: artwork.title,
        artist_id: artwork.artist_id,
        style_id: artwork.style_id,
        medium_id: artwork.medium_id,
        base_price: artwork.base_price,
        status: artwork.status,
    });

    setShowForm(true);

};
const deleteArtwork = (id) => {

    if (!window.confirm("Delete this artwork?")) {
        return;
    }

    api.delete(`/artworks/${id}`)
        .then(() => {

            alert("Artwork deleted successfully!");

            window.location.reload();

        })
        .catch((error) => {

            console.log(error);

            alert("Failed to delete artwork.");

        });

};
    
    return (
    <div>
        <div className="flex justify-between items-center mb-6">
            <h1 className="text-3xl font-bold">
                Artworks
            </h1>

            <button
                onClick={() => setShowForm(!showForm)}
                className="bg-violet-400 hover:bg-violet-500 text-white px-5 py-2 rounded-lg"
            >
                {editingId ? "Update Artwork" : "Save Artwork"}
                + Add Artwork
            </button>
        </div>

        {showForm && (
            <div className="bg-white shadow rounded-lg p-6 mb-6">
                <h2 className="text-xl font-bold mb-4">
                    Add New Artwork
                </h2>

                <form
                    onSubmit={(e) => {
                        e.preventDefault();
                        addArtwork();
                    }}
                >
                    <input
                        type="text"
                        placeholder="Title"
                        value={newArtwork.title}
                        onChange={(e) =>
                            setNewArtwork({
                                ...newArtwork,
                                title: e.target.value,
                            })
                        }
                        className="border rounded w-full p-2 mb-3"
                    />

                    <input
                        type="number"
                        placeholder="Artist ID"
                        value={newArtwork.artist_id}
                        onChange={(e) =>
                            setNewArtwork({
                                ...newArtwork,
                                artist_id: Number(e.target.value),
                            })
                        }
                        className="border rounded w-full p-2 mb-3"
                    />

                    <input
                        type="number"
                        placeholder="Style ID"
                        value={newArtwork.style_id}
                        onChange={(e) =>
                            setNewArtwork({
                                ...newArtwork,
                                style_id: Number(e.target.value),
                            })
                        }
                        className="border rounded w-full p-2 mb-3"
                    />

                    <input
                        type="number"
                        placeholder="Medium ID"
                        value={newArtwork.medium_id}
                        onChange={(e) =>
                            setNewArtwork({
                                ...newArtwork,
                                medium_id: Number(e.target.value),
                            })
                        }
                        className="border rounded w-full p-2 mb-3"
                    />

                    <input
                        type="number"
                        placeholder="Base Price"
                        value={newArtwork.base_price}
                        onChange={(e) =>
                            setNewArtwork({
                                ...newArtwork,
                                base_price: Number(e.target.value),
                            })
                        }
                        className="border rounded w-full p-2 mb-3"
                    />

                    <select
                        value={newArtwork.status}
                        onChange={(e) =>
                            setNewArtwork({
                                ...newArtwork,
                                status: e.target.value,
                            })
                        }
                        className="border rounded w-full p-2 mb-4"
                    >
                        <option value="Available">Available</option>
                        <option value="Sold">Sold</option>
                        <option value="Reserved">Reserved</option>
                    </select>

                    <button
                        type="submit"
                        className="bg-green-500 hover:bg-green-600 text-white px-5 py-2 rounded-lg"
                    >
                        Save Artwork
                    </button>
                </form>
            </div>
        )}

        <table className="w-full bg-white shadow rounded">
            <thead className="bg-pink-200 text-blue-950">
                <tr>
                    <th className="p-3">ID</th>
                    <th className="p-3">Title</th>
                    <th className="p-3">Artist</th>
                    <th className="p-3">Style</th>
                    <th className="p-3">Medium</th>
                    <th className="p-3">Price</th>
                    <th className="p-3">Status</th>
                    <th className="p-3">Actions</th>
                </tr>
            </thead>

            <tbody>
                {artworks.map((artwork) => (
                    <tr
                        key={artwork.artwork_id}
                        className="border-b text-center"
                    >
                        <td className="p-3">{artwork.artwork_id}</td>
                        <td className="p-3">{artwork.title}</td>
                        <td className="p-3">{artwork.artist}</td>
                        <td className="p-3">{artwork.style_name}</td>
                        <td className="p-3">{artwork.medium_name}</td>
                        <td className="p-3">₹ {artwork.base_price}</td>
                        <td className="p-3">{artwork.status}</td>
                        <td className="p-3">
                            <button
                                onClick={() => editArtwork(artwork)}
                                className="bg-rose-300 hover:bg-purple-300 text-black px-3 py-1 rounded mr-2"
                            >
                                Edit
                            </button>

                            <button
                                onClick={() => deleteArtwork(artwork.artwork_id)}
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

export default Artworks;