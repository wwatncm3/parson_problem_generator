# Python Parson's Problem Generator

An interactive web application that generates unlimited randomized Python coding puzzles using Parson's Problems methodology. Created specifically to help my COMP 163 students at NC A&T practice and master the Parsons problems they encounter in Ed STEM, with difficulty levels that match our classroom curriculum progression.

## Background & Motivation

I developed this tool as a CodePath Tech Fellow after observing my students struggling with Parsons problems in Ed STEM during COMP 163 lab sessions. As a senior Computer Science student and Tech Fellow under Professor Dan's team, I recognized that my students needed more practice opportunities outside of the standard platform.

I created the generator by analyzing existing Ed STEM problems and using AI assistance (Gemini) to generate similar complexity problems that align with what we cover in Intro to Python coursework. While the problems may be shorter than those in Ed STEM, they provide students with the essential practice and recall needed to master Parsons problem-solving skills.

## What are Parson's Problems?

Parson's Problems are a type of programming puzzle where students are given code blocks that they must arrange in the correct order to solve a problem. This approach helps learners focus on understanding program logic and structure rather than memorizing syntax.

## Features

- **Three Difficulty Levels**: Easy, Medium, and Hard problems that align with COMP 163 curriculum progression
- **Ed STEM Preparation**: Problems designed with similar complexity to help students prepare for Ed STEM assessments
- **Immediate Feedback**: Instant solution checking with correct answers provided when students get problems wrong
- **Unlimited Practice**: Generate new problems as often as needed for continuous learning
- **Drag & Drop Interface**: Intuitive interface that mirrors the Parsons problem experience
- **Progress Tracking**: Monitor success rates and problem completion statistics
- **No Setup Required**: Pure web-based tool - just open and practice
- **Regular Updates**: Content refreshed bi-weekly around exam and quiz periods

## Getting Started

### Option 1: Direct Download
1. Download the `index.html` file
2. Open it in any modern web browser
3. Start solving problems immediately!

### Option 2: Clone Repository
```bash
git clone https://github.com/wwatncm3/parson_problem_generator.git
cd parson_problem_generator
```
Then open `index.html` in your web browser.

## How to Use

1. **Generate a Problem**: Click one of the problem generation buttons:
   - **Generate New Problem**: Random difficulty
   - **Easy Problem**: Basic variables and simple operations
   - **Medium Problem**: Conditionals and loops
   - **Hard Problem**: Complex logic and nested structures

2. **Solve the Puzzle**: 
   - Drag code blocks from the left panel
   - Drop them in the correct order in the right panel
   - Pay attention to indentation for control structures

3. **Check Your Solution**: 
   - Click "Check Solution" to verify your answer
   - Get instant feedback on correctness
   - View the correct solution if needed

4. **Track Progress**: Monitor your statistics in the header

## Problem Types

### Easy Problems
- Variable assignment and basic operations
- Simple string concatenation  
- Basic conditional statements
- Perfect for absolute beginners

### Medium Problems
- If-else statements
- For and while loops
- List operations and string methods
- Great for students learning control flow

### Hard Problems  
- Nested conditional statements
- Complex loop structures
- Multiple variable operations
- Ideal for reinforcing advanced concepts

## Technical Details

- **Framework**: Pure vanilla JavaScript - no dependencies
- **Compatibility**: Modern web browsers (Chrome, Firefox, Safari, Edge)
- **Storage**: Uses localStorage for progress tracking
- **Responsive**: CSS Grid and Flexbox for mobile-friendly design

## Educational Benefits

- **Reduces Cognitive Load**: Students focus on logic rather than syntax
- **Builds Pattern Recognition**: Helps students recognize common programming patterns
- **Immediate Feedback**: Quick validation encourages experimentation
- **Self-Paced Learning**: Students can work at their own speed
- **Confidence Building**: Success with arrangement builds confidence for writing code from scratch

## Usage in Classroom

### For My COMP 163 Students at NC A&T
- **Ed STEM Preparation**: Practice problems similar to those you'll encounter in Ed STEM assessments
- **Supplement Lab Learning**: Additional practice between our lab sessions
- **Exam & Quiz Prep**: Use before assessments to reinforce Parsons problem-solving skills
- **Self-Paced Learning**: Work through problems at your own speed outside of class
- **Confidence Building**: Master the format before tackling more complex Ed STEM problems

### For Fellow CodePath Tech Fellows & Instructors
- **Student-Centered Design**: Tool created from direct observation of student struggles
- **Homework Assignments**: Assign specific difficulty levels to match weekly topics
- **Lab Warm-ups**: Start sessions with quick Parsons problem practice
- **Assessment Preparation**: Help students prepare for Ed STEM evaluations
- **Office Hours Support**: Use during tutoring sessions to diagnose problem areas

## Contributing

Contributions are welcome! Here are ways you can help:

- **Add New Problems**: Create more varied problem types
- **Improve UI/UX**: Enhance the user interface
- **Add Features**: Implement timer, hints, or difficulty progression
- **Fix Bugs**: Report and fix any issues you find
- **Documentation**: Improve README or add code comments

### Adding New Problems

Problems are stored in the `problemBank` array. Each problem needs:

```javascript
{
    difficulty: 'easy|medium|hard',
    title: 'Problem Name',
    description: 'What the code should accomplish',
    instructions: 'Specific directions for the student', 
    blocks: ['array', 'of', 'code', 'blocks', 'including', 'distractors'],
    solution: [
        { "code line": [] }, // Top-level statement
        { "if condition:": ["    indented", "    statements"] } // Block with children
    ]
}
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Created by me, Will Walton III - CodePath Tech Fellow & Senior CS student at NC A&T
- Developed for my COMP 163 Intro to Python students under Professor Dan's team
- Built in response to my observation of student struggles with Ed STEM Parsons problems
- Enhanced with AI assistance (Gemini) to generate curriculum-appropriate problems
- Special thanks to CodePath, Professor Dan's Tech Fellow team, and my fellow NC A&T educators

## Updates & Maintenance

I actively maintain this tool with updates planned bi-weekly, particularly around:
- Exam preparation periods
- Quiz schedules  
- Major assignment deadlines
- New curriculum topics I introduce in COMP 163

Check back regularly for new problem types and difficulty adjustments based on my classroom observations.

## Contact

- **GitHub**: [@wwatncm3](https://github.com/wwatncm3)
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Questions**: Reach out if you're a fellow educator interested in adapting this for your curriculum

---

**Happy coding and teaching!**
