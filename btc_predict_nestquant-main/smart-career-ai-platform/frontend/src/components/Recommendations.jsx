import React, { useEffect, useState } from 'react';
import { getRecommendations } from '../services/api';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Recommendations({ userText, userId }) {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (userText && userText.trim().length > 10) {
      fetchRecommendations();
    }
  }, [userText, userId]);

  const fetchRecommendations = async () => {
    setLoading(true);
    setError('');

    try {
      const response = await getRecommendations(userText, userId, 5);
      if (response.success) {
        setResults(response.recommendations || []);
      } else {
        setError('Failed to get recommendations');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to get recommendations');
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center justify-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
          <span className="ml-4 text-gray-600">Analyzing and generating recommendations...</span>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="p-4 bg-red-50 text-red-700 rounded-md">
          {error}
        </div>
      </div>
    );
  }

  if (!results || results.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow-lg p-6">
        <p className="text-gray-600 text-center py-8">
          No recommendations available. Please upload a resume or enter your skills.
        </p>
      </div>
    );
  }

  // Prepare data for chart
  const chartData = results.map((r, idx) => ({
    name: r.title.length > 20 ? r.title.substring(0, 20) + '...' : r.title,
    fullName: r.title,
    score: r.score,
    index: idx + 1,
  }));

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <h2 className="text-2xl font-bold mb-6 text-gray-800">Top Career Recommendations</h2>
      
      {/* Chart Visualization */}
      <div className="mb-8">
        <ResponsiveContainer width="100%" height={300}>
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

      {/* List of Recommendations */}
      <div className="space-y-4">
        {results.map((result, idx) => (
          <div
            key={idx}
            className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between mb-2">
              <h3 className="text-xl font-semibold text-gray-800">
                #{idx + 1} {result.title}
              </h3>
              <span className="bg-primary-100 text-primary-800 px-3 py-1 rounded-full text-sm font-semibold">
                {result.score}% Match
              </span>
            </div>
            {result.description && (
              <p className="text-gray-600 mt-2">{result.description}</p>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Recommendations;

