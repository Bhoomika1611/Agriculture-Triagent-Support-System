# 🌾 Agri-Support-System

An AI-powered agricultural support system that leverages CrewAI, LangChain, and Retrieval-Augmented Generation (RAG) to provide intelligent farming advice, disease diagnostics, and agricultural policy guidance.

## 🎯 Features

- **Crop Advisory**: Get personalized crop farming recommendations and best practices
- **Disease Identification**: Identify potential crop diseases and treatment solutions
- **Policy Guidance**: Receive information about agricultural policies and regulations
- **Multi-Agent AI System**: Powered by CrewAI with specialized agents for different agricultural domains
- **RAG Integration**: Context-aware responses using ChromaDB vector database
- **Web Interface**: User-friendly Streamlit dashboard for easy interaction
- **CLI Support**: Command-line interface for direct queries

## 🏗️ Architecture

### Core Components

- **agents.py**: Defines specialized AI agents (crop advisor, disease expert, policy advisor, priority agent)
- **tasks.py**: Defines AI tasks that agents execute
- **crew_setup.py**: Orchestrates the multi-agent crew
- **rag_setup.py**: Handles Retrieval-Augmented Generation setup
- **data_collector.py**: Manages data collection and preprocessing

### User Interfaces

- **app.py**: Streamlit web application (main UI)
- **main.py**: Command-line interface

### Infrastructure

- **Docker**: Containerized deployment (Dockerfile included)
- **Terraform**: Infrastructure-as-code configuration
- **ChromaDB**: Vector database for embeddings and similarity search

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or conda for package management
- API keys for LLM services (Groq API recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Agri-Support-System
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env  # Create from template if available
   ```
   
   Add your API keys to `.env`:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 📖 Usage

### Web Interface (Streamlit)

Start the web application:
```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and interact with the AI system through the user-friendly interface.

### Command-Line Interface

Run queries directly from the terminal:
```bash
python main.py
```

Enter your agriculture-related question when prompted.

## 📊 Project Structure

```
Agri-Support-System/
├── agents.py              # AI agent definitions
├── app.py                 # Streamlit web interface
├── crew_setup.py          # Multi-agent crew orchestration
├── data_collector.py      # Data collection utilities
├── main.py                # CLI entry point
├── rag_setup.py           # RAG pipeline setup
├── tasks.py               # Task definitions for agents
├── requirements.txt       # Python dependencies
├── data/
│   └── agriculture_docs.txt  # Agricultural documentation
├── vector_db/
│   └── chroma.sqlite3     # Vector database storage
├── docker/
│   └── Dockerfile         # Docker containerization
├── terraform/
│   └── main.tf            # Infrastructure configuration
└── docs/                  # Documentation files
```

## 🔧 Technologies Used

- **CrewAI**: Multi-agent orchestration framework
- **LangChain**: LLM framework and utilities
- **Groq**: Fast LLM inference
- **ChromaDB**: Vector database for embeddings
- **Streamlit**: Web application framework
- **Hugging Face**: Embeddings and NLP models
- **FAISS**: Similarity search library
- **BeautifulSoup4**: Web scraping capabilities

## 🐳 Docker Deployment

Build and run the application in Docker:

```bash
docker build -f docker/Dockerfile -t agri-support-system .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key agri-support-system
```

## 📦 Infrastructure (Terraform)

Deploy infrastructure using Terraform:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

## 🗄️ Data Management

The system uses ChromaDB for vector storage, enabling efficient semantic search over agricultural documents. Documents are stored in `data/agriculture_docs.txt` and indexed for retrieval-augmented generation.

### Vector Database

- **Location**: `vector_db/`
- **Type**: ChromaDB with SQLite backend
- **Purpose**: Store and retrieve relevant agricultural context

## 🔐 Environment Variables

Configure the following in your `.env` file:

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | API key for Groq LLM service |
| `HUGGINGFACE_API_KEY` | (Optional) Hugging Face API key |

## 📝 Example Queries

- "How should I optimize my wheat crop this season?"
- "What are the symptoms of wheat rust disease?"
- "What agricultural subsidies am I eligible for?"
- "How can I improve soil health for my farm?"

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- CrewAI framework for multi-agent orchestration
- Groq for fast LLM inference
- The open-source community for various libraries and tools

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on the GitHub repository
- Contact the development team

## 🌍 Future Enhancements

- [ ] Multi-language support
- [ ] Real-time crop monitoring integration
- [ ] Weather API integration
- [ ] Mobile application
- [ ] Predictive analytics for crop yield
- [ ] Integration with agricultural IoT devices
- [ ] Community forum for farmers

---

**Happy Farming! 🌱**
