import React, { useState } from 'react';
import ResumeUploader from '../components/ResumeUploader';
import Recommendations from '../components/Recommendations';

function Home() {
  const [userText, setUserText] = useState('');
  const [userId, setUserId] = useState(null);

  const handleUploadSuccess = (extractedText, id) => {
    setUserText(extractedText);
    setUserId(id);
  };

  const handleTextSubmit = (text, id) => {
    setUserText(text);
    setUserId(id);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Smart Career AI Platform
          </h1>
          <p className="text-xl text-gray-600">
            Get personalized career recommendations based on your skills and experience
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div>
            <ResumeUploader
              onUploadSuccess={handleUploadSuccess}
              onTextSubmit={handleTextSubmit}
            />
          </div>
          
          <div>
            {userText && (
              <Recommendations userText={userText} userId={userId} />
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;

