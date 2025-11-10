import React, { useEffect, useState } from 'react';
import { getUserRecommendations, healthCheck } from '../services/api';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line } from 'recharts';

function Dashboard() {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [userId, setUserId] = useState(null);
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    checkApiHealth();
  }, []);

  const checkApiHealth = async () => {
    try {
      const status = await healthCheck();
      setApiStatus('online');
    } catch (err) {
      setApiStatus('offline');
    }
  };

  const handleFetchRecommendations = async () => {
    if (!userId) {
      setError('Please enter a user ID');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await getUserRecommendations(userId);
      if (response.success) {
        setRecommendations(response.recommendations || []);
      } else {
        setError('Failed to fetch recommendations');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to fetch recommendations');
      setRecommendations([]);
    } finally {
      setLoading(false);
    }
  };

  const chartData = recommendations.map((rec, idx) => ({
    name: rec.job_title.length > 15 ? rec.job_title.substring(0, 15) + '...' : rec.job_title,
    fullName: rec.job_title,
    score: rec.score,
    date: new Date(rec.created_at).toLocaleDateString(),
  }));

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Dashboard
          </h1>
          <p className="text-xl text-gray-600">
            View your career recommendations and analytics
          </p>
        </div>

        {/* API Status */}
        <div className="mb-6">
          <div className={`inline-flex items-center px-4 py-2 rounded-md ${
            apiStatus === 'online' ? 'bg-green-100 text-green-800' : 
            apiStatus === 'offline' ? 'bg-red-100 text-red-800' : 
            'bg-yellow-100 text-yellow-800'
          }`}>
            <span className="w-2 h-2 rounded-full mr-2 bg-current animate-pulse"></span>
            API Status: {apiStatus === 'online' ? 'Online' : apiStatus === 'offline' ? 'Offline' : 'Checking...'}
          </div>
        </div>

        {/* User ID Input */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex gap-4">
            <input
              type="number"
              value={userId || ''}
              onChange={(e) => setUserId(e.target.value ? parseInt(e.target.value) : null)}
              placeholder="Enter User ID"
              className="flex-1 px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
            <button
              onClick={handleFetchRecommendations}
              disabled={loading || !userId}
              className="bg-primary-600 text-white px-6 py-2 rounded-md hover:bg-primary-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? 'Loading...' : 'Fetch Recommendations'}
            </button>
          </div>
        </div>

        {error && (
          <div className="bg-red-50 text-red-700 p-4 rounded-md mb-6">
            {error}
          </div>
        )}

        {recommendations.length > 0 && (
          <>
            {/* Chart Visualization */}
            <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
              <h2 className="text-2xl font-bold mb-4 text-gray-800">Recommendations Overview</h2>
              <ResponsiveContainer width="100%" height={400}>
                <BarChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis 
                    dataKey="name" 
                    angle={-45}
                    textAnchor="end"
                    height={100}
                    interval={0}
                  />
                  <YAxis 
                    label={{ value: 'Match Score (%)', angle: -90, position: 'insideLeft' }}
                  />
                  <Tooltip 
                    formatter={(value, name, props) => [
                      `${value}%`,
                      props.payload.fullName
                    ]}
                  />
                  <Legend />
                  <Bar dataKey="score" fill="#0ea5e9" name="Match Score" />
                </BarChart>
              </ResponsiveContainer>
            </div>

            {/* Recommendations List */}
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold mb-4 text-gray-800">All Recommendations</h2>
              <div className="space-y-4">
                {recommendations.map((rec) => (
                  <div
                    key={rec.id}
                    className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
                  >
                    <div className="flex items-start justify-between mb-2">
                      <h3 className="text-xl font-semibold text-gray-800">
                        {rec.job_title}
                      </h3>
                      <span className="bg-primary-100 text-primary-800 px-3 py-1 rounded-full text-sm font-semibold">
                        {rec.score}% Match
                      </span>
                    </div>
                    <p className="text-sm text-gray-500">
                      Added on: {new Date(rec.created_at).toLocaleString()}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          </>
        )}

        {!loading && recommendations.length === 0 && userId && !error && (
          <div className="bg-white rounded-lg shadow-lg p-6 text-center">
            <p className="text-gray-600">
              No recommendations found for this user. Try getting recommendations first on the home page.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;

