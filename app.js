import { useState } from "react";

export default function App() {
  const [text, setText] = useState("");
  const [translatedText, setTranslatedText] = useState("");
  const [language, setLanguage] = useState("French");

  const handleTranslate = async () => {
    const response = await fetch("http://127.0.0.1:5000/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, target_lang: language }),
    });

    const data = await response.json();
    setTranslatedText(data.translated_text || "Translation failed.");
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-5">
      <h1 className="text-2xl font-bold mb-4">Language Translator</h1>
      <textarea
        className="border p-2 w-full max-w-lg h-32"
        placeholder="Enter text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <select
        className="border p-2 my-3"
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
      >
        <option value="French">French</option>
        <option value="Spanish">Spanish</option>
        <option value="German">German</option>
      </select>
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded"
        onClick={handleTranslate}
      >
        Translate
      </button>
      {translatedText && (
        <p className="mt-4 p-3 bg-white border rounded">{translatedText}</p>
      )}
    </div>
  );
}
