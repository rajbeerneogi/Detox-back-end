Detox — AI-Powered Water Quality Assessment
Detox is an AI-assisted water quality assessment platform designed to make preliminary water analysis more accessible through image-based visual inspection. Developed for the Xylem Global Student Innovation Challenge 2026, the project explores how artificial intelligence and modern web technologies can support water-quality awareness, environmental monitoring, and informed decision-making.

The platform consists of a React-based frontend and a Python FastAPI backend integrated with Google's Gemini AI model. Together, these components provide a workflow in which users can submit photographs of water samples and receive an AI-generated assessment of their visible characteristics.
Project Overview
Water quality is an important environmental and public-health concern, but access to testing facilities and specialised equipment can be limited. Detox aims to provide an accessible first step by using AI to interpret visible characteristics in water-sample images.

Users can interact with the application through its frontend, submit a water-sample image, and send it to the backend for processing. The backend validates and prepares the image before passing it to the AI analysis service. The resulting observations are then returned to the application for presentation.

Detox is designed as a complementary visual-assessment tool, not a replacement for laboratory testing or professional water-quality instruments.
Frontend — User Interface
The frontend is built using React and Vite, providing the user-facing interface through which users interact with the Detox platform.

Its intended responsibilities include:
- Providing an accessible and intuitive interface for water-sample analysis.
- Allowing users to submit water-sample photographs.
- Supporting a workflow for image submission, analysis, and result presentation.
- Communicating with the backend API to request analysis.
- Presenting AI-generated observations and relevant assessment information.
- Providing a foundation for future features, including structured water-quality data uploads and visualisation.
Backend — AI Processing and Analysis
The backend is developed using Python and FastAPI. It handles image uploads, validation, preprocessing, and communication with the AI analysis service.

Its main responsibilities include:
- Receiving water-sample images through API endpoints.
- Validating supported image formats and file constraints.
- Processing images using Python imaging tools.
- Integrating with Google's Gemini AI through the Google GenAI SDK.
- Generating AI-assisted descriptions of visible water characteristics.
- Returning analysis results and relevant limitations through API responses.
- Providing an API structure that can be extended with additional water-quality assessment features.
AI-Powered Visual Assessment
Detox uses Google's Gemini AI model to interpret visual information in submitted water-sample photographs.

Depending on image quality and visible characteristics, the system can provide observations relating to:
- Apparent water clarity and cloudiness.
- Visible suspended particles or sediment.
- Unusual colouration.
- Surface appearance and visible films.
- Other noticeable visual characteristics.
The AI-generated assessment is intended to help users identify visible features that may warrant further investigation.
Technology Stack
Component	Technology
Frontend	React
Frontend tooling	Vite
Backend framework	Python, FastAPI
AI integration	Google Gemini
AI SDK	Google GenAI
Image processing	Pillow (PIL)
API communication	HTTP / REST

Scientific Scope and Limitations
An important design principle behind Detox is distinguishing between what AI can observe in an image and what requires actual measurement.

A photograph alone cannot reliably determine numerical pH, total dissolved solids (TDS), dissolved oxygen, heavy-metal concentrations, bacterial contamination, or whether water is safe to drink.

For this reason, Detox focuses on visual observations rather than presenting unsupported laboratory measurements.

The platform is intended to complement, not replace:
- Certified laboratory water testing.
- Calibrated water-quality meters and sensors.
- Professional environmental assessment.
- Established drinking-water safety standards.
Clear-looking water is not necessarily safe to drink. AI-generated observations should therefore be treated as preliminary information, not a declaration of water safety.
Future Development
Detox is designed with room for further development. Potential improvements include:
- Integration with real water-quality sensors and handheld testing devices.
- CSV uploads for structured water-quality measurements.
- Comparison of measured values against recognised water-quality guidelines.
- Historical analysis and water-quality trend visualisation.
- Improved image-analysis workflows.
- More detailed reporting and recommendations.
- Deployment of the frontend and backend for public access.
These are development goals, not claims that every feature is already implemented.
Project Vision
The long-term vision of Detox is to explore how accessible AI tools can support environmental awareness and make water-quality information easier to understand.

By combining computer vision, AI-assisted interpretation, and a scalable web application architecture, Detox aims to create a foundation for more accessible and data-informed water-quality assessment.

Built as a student innovation project for the Xylem Global Student Innovation Challenge 2026 
#Contuined development Ideas include :-
1) Adding .CSV file processing
2) Making its processor faster 
3) Improving accuracy 
