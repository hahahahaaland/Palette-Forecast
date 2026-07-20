import { useEffect, useState } from "react";
import api from "../services/api";

function Analytics() {

    const [revenue, setRevenue] = useState({});
    const [topArtist, setTopArtist] = useState({});
    const [topStyle, setTopStyle] = useState({});
    const [topMedium, setTopMedium] = useState({});
    const [giftWrap, setGiftWrap] = useState({});
    const [commissions, setCommissions] = useState({});
    const [status, setStatus] = useState({});

    useEffect(() => {

        api.get("/analytics/revenue")
            .then((res) => setRevenue(res.data));

        api.get("/analytics/top-artist")
            .then((res) => setTopArtist(res.data));

        api.get("/analytics/top-style")
            .then((res) => setTopStyle(res.data));

        api.get("/analytics/top-medium")
            .then((res) => setTopMedium(res.data));

        api.get("/analytics/gift-wrap")
            .then((res) => setGiftWrap(res.data));

        api.get("/analytics/commissions")
            .then((res) => setCommissions(res.data));

        api.get("/analytics/status")
            .then((res) => setStatus(res.data));

    }, []);

    return (

        <div>

            <h1 className="text-3xl font-bold mb-8">
                Analytics Dashboard
            </h1>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Total Revenue
                    </h3>
                    <p className="text-3xl font-bold text-green-600">
                        ₹ {revenue.total_revenue}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Top Artist
                    </h3>
                    <p className="text-2xl font-semibold">
                        {topArtist.top_artist}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Top Style
                    </h3>
                    <p className="text-2xl font-semibold">
                        {topStyle.top_style}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Top Medium
                    </h3>
                    <p className="text-2xl font-semibold">
                        {topMedium.top_medium}
                    </p>
                </div>

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Artwork Status
                    </h3>

                    {Object.keys(status).length > 0 ? (
                        Object.entries(status).map(([key, value]) => (
                            <p key={key}>
                                <strong>{key}:</strong> {value}
                            </p>
                        ))
                    ) : (
                        <p>No data</p>
                    )}

                </div>

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Gift Wrap Orders
                    </h3>

                    {Object.keys(giftWrap).length > 0 ? (
                        Object.entries(giftWrap).map(([key, value]) => (
                            <p key={key}>
                                <strong>{key}:</strong> {value}
                            </p>
                        ))
                    ) : (
                        <p>No data</p>
                    )}

                </div>

                <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-gray-500 mb-2">
                        Commission Orders
                    </h3>

                    {Object.keys(commissions).length > 0 ? (
                        Object.entries(commissions).map(([key, value]) => (
                            <p key={key}>
                                <strong>{key}:</strong> {value}
                            </p>
                        ))
                    ) : (
                        <p>No data</p>
                    )}

                </div>

            </div>

        </div>

    );

}

export default Analytics;