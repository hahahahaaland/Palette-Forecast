import { useEffect, useState } from "react";
import api from "../services/api";

function Artworks() {

    const [artworks, setArtworks] = useState([]);

    useEffect(() => {

        api.get("/artworks")
            .then((response) => {
                setArtworks(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, []);

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">
                Artworks
            </h1>

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

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default Artworks;