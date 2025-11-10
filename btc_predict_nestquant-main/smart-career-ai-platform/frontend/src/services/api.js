import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const uploadResume = async (file, email = 'anonymous@example.com') => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('email', email);
  
  const response = await api.post('/upload_resume', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  
  return response.data;
};

export const uploadText = async (text, email = 'anonymous@example.com') => {
  const response = await api.post('/upload_text', {
    text,
    email,
  });
  
  return response.data;
};

export const getRecommendations = async (text, userId = null, topN = 5) => {
  const response = await api.post('/recommend', {
    text,
    user_id: userId,
    top_n: topN,
  });
  
  return response.data;
};

export const getUserRecommendations = async (userId) => {
  const response = await api.get(`/recommendations/${userId}`);
  return response.data;
};

export const healthCheck = async () => {
  const response = await api.get('/health');
  return response.data;
};

export default api;

