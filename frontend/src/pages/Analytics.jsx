import { useEffect, useState } from "react";
import api from "../services/api";

function Analytics() {

    const [revenue, setRevenue] = useState({});
    const [topArtist, setTopArtist] = useState({});
    const [topStyle, setTopStyle] = useState({});
    const [topMedium, setTopMedium] = useState({});
    const [giftWrap, setGiftWrap] = useState([]);
    const [commissions, setCommissions] = useState([]);
    const [status, setStatus] = useState([]);

    useEffect(() => {

        api.get("/analytics/revenue").then(res => setRevenue(res.data));
        api.get("/analytics/top-artist").then(res => setTopArtist(res.data));
        api.get("/analytics/top-style").then(res => setTopStyle(res.data));
        api.get("/analytics/top-medium").then(res => setTopMedium(res.data));
        api.get("/analytics/gift-wrap").then(res => setGiftWrap(res.data));
        api.get("/analytics/commissions").then(res => setCommissions(res.data));
        api.get("/analytics/artwork-status").then(res => setStatus(res.data));

    }, []);

    return (

        <div>

            <h1 className="text-3xl font-bold mb-8">
                Analytics
            </h1>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-6">

                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500">Revenue</h3>
                    <p className="text-2xl font-bold">
                        ₹ {revenue.total_revenue}
                    </p>
                </div>

                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500">Top Artist</h3>
                    <p className="text-xl font-semibold">
                        {topArtist.name}
                    </p>
                </div>

                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500">Top Style</h3>
                    <p className="text-xl font-semibold">
                        {topStyle.style_name}
                    </p>
                </div>

                <div className="bg-white p-6 rounded shadow">
                    <h3 className="text-gray-500">Top Medium</h3>
                    <p className="text-xl font-semibold">
                        {topMedium.medium_name}
                    </p>
                </div>

            </div>

        </div>

    );

}

export default Analytics;