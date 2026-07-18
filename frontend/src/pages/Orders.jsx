import { useEffect, useState } from "react";
import api from "../services/api";

function Orders() {

    const [orders, setOrders] = useState([]);

    useEffect(() => {

        api.get("/orders")
            .then((response) => {
                setOrders(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

    }, []);

    return (

        <div>

            <h1 className="text-3xl font-bold mb-6">
                Orders
            </h1>

            <table className="w-full bg-white shadow rounded">

                <thead className="bg-pink-200 text-blue-950">

                    <tr>
                        <th className="p-3">ID</th>
                        <th className="p-3">Artwork</th>
                        <th className="p-3">Customer</th>
                        <th className="p-3">Price</th>
                        <th className="p-3">Gift Wrap</th>
                        <th className="p-3">Commission</th>
                    </tr>

                </thead>

                <tbody>

                    {orders.map((order) => (

                        <tr
                            key={order.order_id}
                            className="border-b text-center"
                        >

                            <td className="p-3">{order.order_id}</td>
                            <td className="p-3">{order.title}</td>
                            <td className="p-3">{order.customer_name}</td>
                            <td className="p-3">₹ {order.final_price}</td>
                            <td className="p-3">
                                {order.gift_wrap ? "Yes" : "No"}
                            </td>
                            <td className="p-3">
                                {order.commission_order ? "Yes" : "No"}
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </div>

    );

}

export default Orders;