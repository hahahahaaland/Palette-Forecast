import { useEffect, useState } from "react";
import api from "../services/api";

function Analytics() {
    const [revenue, setRevenue] = useState(0);
    const [topArtist, setTopArtist] = useState("");
    const [topStyle, setTopStyle] = useState("");
    const [topMedium, setTopMedium] = useState("");
    const [status, setStatus] = useState({});
    const [giftWrap, setGiftWrap] = useState({});
    const [commissions, setCommissions] = useState({});

    useEffect(() => {
        api.get("/analytics/revenue")
            .then((res) => setRevenue(res.data.total_revenue));

        api.get("/analytics/top-artist")
            .then((res) => setTopArtist(res.data.top_artist));

        api.get("/analytics/top-style")
            .then((res) => setTopStyle(res.data.top_style));

        api.get("/analytics/top-medium")
            .then((res) => setTopMedium(res.data.top_medium));

        api.get("/analytics/status")
            .then((res) => setStatus(res.data));

        api.get("/analytics/gift-wrap")
            .then((res) => setGiftWrap(res.data));

        api.get("/analytics/commissions")
            .then((res) => setCommissions(res.data));
    }, []);

    return (
        <div>
            <h1 className="text-3xl font-bold mb-6">
                Analytics Dashboard
            </h1>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">Total Revenue</h2>
                    <p className="text-2xl text-green-600">
                        ₹ {revenue}
                    </p>
                </div>

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">Top Artist</h2>
                    <p>{topArtist}</p>
                </div>

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">Top Style</h2>
                    <p>{topStyle}</p>
                </div>

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">Top Medium</h2>
                    <p>{topMedium}</p>
                </div>

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">
                        Artwork Status
                    </h2>

                    {Object.entries(status).map(([key, value]) => (
                        <p key={key}>
                            {key}: {value}
                        </p>
                    ))}
                </div>

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">
                        Gift Wrap Orders
                    </h2>

                    {Object.entries(giftWrap).map(([key, value]) => (
                        <p key={key}>
                            {key}: {value}
                        </p>
                    ))}
                </div>

                <div className="bg-white shadow rounded-lg p-5">
                    <h2 className="font-bold text-lg mb-2">
                        Commission Orders
                    </h2>

                    {Object.entries(commissions).map(([key, value]) => (
                        <p key={key}>
                            {key}: {value}
                        </p>
                    ))}
                </div>

            </div>
        </div>
    );
}

export default Analytics;