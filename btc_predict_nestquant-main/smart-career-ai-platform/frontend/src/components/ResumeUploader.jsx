import React, { useState } from 'react';
import { uploadResume, uploadText } from '../services/api';

function ResumeUploader({ onUploadSuccess, onTextSubmit }) {
  const [file, setFile] = useState(null);
  const [text, setText] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [mode, setMode] = useState('upload'); // 'upload' or 'text'

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError('');
    } else {
      setError('Please select a valid PDF file');
      setFile(null);
    }
  };

  const handleFileUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setError('Please select a PDF file');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const result = await uploadResume(file, email || 'anonymous@example.com');
      if (result.success) {
        onUploadSuccess(result.extracted_text, result.user_id);
        setFile(null);
        setEmail('');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to upload resume');
    } finally {
      setLoading(false);
    }
  };

  const handleTextSubmit = async (e) => {
    e.preventDefault();
    if (!text.trim()) {
      setError('Please enter some text about your skills or experience');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const result = await uploadText(text, email || 'anonymous@example.com');
      if (result.success) {
        onTextSubmit(text, result.user_id);
        setText('');
        setEmail('');
      }
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to process text');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
      <div className="flex space-x-4 mb-4 border-b">
        <button
          onClick={() => setMode('upload')}
          className={`px-4 py-2 font-semibold ${
            mode === 'upload'
              ? 'text-primary-600 border-b-2 border-primary-600'
              : 'text-gray-600 hover:text-primary-600'
          }`}
        >
          Upload Resume
        </button>
        <button
          onClick={() => setMode('text')}
          className={`px-4 py-2 font-semibold ${
            mode === 'text'
              ? 'text-primary-600 border-b-2 border-primary-600'
              : 'text-gray-600 hover:text-primary-600'
          }`}
        >
          Enter Skills
        </button>
      </div>

      <div className="mb-4">
        <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-2">
          Email (optional)
        </label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="your.email@example.com"
          className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
        />
      </div>

      {mode === 'upload' ? (
        <form onSubmit={handleFileUpload}>
          <div className="mb-4">
            <label htmlFor="file" className="block text-sm font-medium text-gray-700 mb-2">
              Upload PDF Resume
            </label>
            <input
              type="file"
              id="file"
              accept=".pdf"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-primary-50 file:text-primary-700 hover:file:bg-primary-100"
            />
          </div>

          {error && (
            <div className="mb-4 p-3 bg-red-50 text-red-700 rounded-md">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading || !file}
            className="w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
          >
            {loading ? 'Processing...' : 'Upload and Analyze'}
          </button>
        </form>
      ) : (
        <form onSubmit={handleTextSubmit}>
          <div className="mb-4">
            <label htmlFor="text" className="block text-sm font-medium text-gray-700 mb-2">
              Enter your skills, experience, or career interests
            </label>
            <textarea
              id="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="e.g., I have 3 years of experience in Python, machine learning, and data analysis. I'm interested in working with AI and building predictive models..."
              rows="6"
              className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            />
          </div>

          {error && (
            <div className="mb-4 p-3 bg-red-50 text-red-700 rounded-md">
              {error}
            </div>
          )}

          <button
            type="submit"
            disabled={loading || !text.trim()}
            className="w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
          >
            {loading ? 'Processing...' : 'Get Recommendations'}
          </button>
        </form>
      )}
    </div>
  );
}

export default ResumeUploader;

