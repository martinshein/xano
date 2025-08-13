# Contributing to Xano Documentation Knowledge Base

Thank you for your interest in contributing to the Xano Documentation Knowledge Base! This guide will help you get started.

## 🤝 Ways to Contribute

### 1. Documentation Improvements
- Fix typos, grammar, or formatting issues
- Clarify existing documentation
- Add missing information
- Update outdated content

### 2. Code Examples
- Add new code examples
- Improve existing examples
- Add comments to code for clarity
- Create complete working examples

### 3. New Content
- Write new guides or tutorials
- Create reference materials
- Add troubleshooting scenarios
- Document best practices

### 4. Organization
- Suggest better categorization
- Improve file naming
- Enhance cross-references
- Update index files

## 📋 Before Contributing

1. **Check existing issues** to avoid duplicate work
2. **Read the documentation** to understand the structure
3. **Follow the style guide** for consistency
4. **Test your changes** if they include code

## 🚀 Getting Started

### 1. Fork the Repository
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/xano.git
cd xano
```

### 2. Create a Branch
```bash
# Create a descriptive branch name
git checkout -b feature/add-webhook-examples
# or
git checkout -b fix/typo-in-api-docs
```

### 3. Make Your Changes
- Edit files in your preferred editor
- Follow the existing format and style
- Add YAML frontmatter to new files
- Keep changes focused and atomic

### 4. Commit Your Changes
```bash
# Stage your changes
git add .

# Commit with a clear message
git commit -m "Add webhook integration examples for Stripe"
# or
git commit -m "Fix typo in database operations guide"
```

### 5. Push and Create PR
```bash
# Push to your fork
git push origin feature/add-webhook-examples

# Create a Pull Request on GitHub
```

## 📝 Style Guide

### File Structure
```yaml
---
title: Clear, Descriptive Title
category: appropriate-category
tags:
- relevant
- tags
- max-5
has_code_examples: true/false
last_updated: YYYY-MM-DD
---

# Title

Brief introduction...

## Main Section

Content...

### Subsection

More content...
```

### Code Examples
```javascript
// Always include language identifier
// Add comments for clarity
function exampleFunction(param) {
  // Explain what this does
  return param * 2;
}
```

### Writing Style
- **Be Clear**: Use simple, direct language
- **Be Concise**: Get to the point quickly
- **Be Complete**: Include all necessary information
- **Be Consistent**: Follow existing patterns

### Formatting
- Use **bold** for emphasis
- Use `code` for inline code
- Use proper heading hierarchy (# ## ###)
- Include code language identifiers
- Add alt text to images

## 🧪 Testing

### For Code Examples
1. Ensure code is syntactically correct
2. Test in actual Xano environment if possible
3. Include all necessary context
4. Add error handling where appropriate

### For Documentation
1. Check all links work
2. Verify code blocks render correctly
3. Ensure YAML frontmatter is valid
4. Preview in markdown viewer

## 📊 Pull Request Guidelines

### PR Title
Use conventional commit format:
- `feat:` New feature or content
- `fix:` Bug fix or correction
- `docs:` Documentation only changes
- `style:` Formatting changes
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

Examples:
- `feat: Add GraphQL integration examples`
- `fix: Correct authentication flow diagram`
- `docs: Update API rate limiting section`

### PR Description
Include:
1. **What** - Brief description of changes
2. **Why** - Reason for the changes
3. **How** - Technical approach (if relevant)
4. **Testing** - How you tested the changes
5. **Screenshots** - If visual changes

### PR Checklist
- [ ] Follows style guide
- [ ] Includes proper YAML frontmatter
- [ ] Code examples are tested
- [ ] Links are working
- [ ] No duplicate content
- [ ] Commits are clean and descriptive
- [ ] Branch is up to date with main

## 🐛 Reporting Issues

### Bug Reports
Include:
1. Description of the issue
2. File path and line number
3. Expected vs actual behavior
4. Steps to reproduce (if applicable)
5. Suggested fix (if known)

### Feature Requests
Include:
1. Clear description of the feature
2. Use case and benefits
3. Examples from other documentation
4. Proposed implementation (optional)

## 💬 Communication

### Where to Ask Questions
- **GitHub Issues**: For bugs and features
- **GitHub Discussions**: For general questions
- **Pull Requests**: For code review

### Response Times
- Issues: 2-3 business days
- PRs: 3-5 business days
- Discussions: Community-driven

## 🏆 Recognition

Contributors will be:
- Listed in the README
- Mentioned in release notes
- Given credit in commit history

## 📜 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Public or private harassment
- Publishing private information
- Other unprofessional conduct

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions make this knowledge base better for everyone. Whether it's fixing a typo or adding entire sections, every contribution matters!

---

**Questions?** Open an issue or discussion thread.
**Ready to contribute?** Fork, branch, and PR!
**Need help?** Tag @martinshein in your issue or PR.