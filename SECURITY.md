# Security Policy

## Supported Versions

We actively support the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly. We take security seriously and appreciate your help in keeping our users safe.

### How to Report

1. **Do not** create a public GitHub issue for the vulnerability
2. Email security concerns to: [security@yourproject.com](mailto:security@yourproject.com)
3. Include detailed information about:
   - The vulnerability description
   - Steps to reproduce
   - Potential impact
   - Any suggested fixes

### What to Expect

- **Acknowledgment**: We'll acknowledge receipt within 48 hours
- **Investigation**: We'll investigate and provide regular updates
- **Resolution**: We'll work on a fix and coordinate disclosure
- **Credit**: We'll credit you (if desired) when the issue is resolved

## Security Considerations

This project processes PDF documents locally and does not transmit data to external services. However, please be aware of the following:

### Input Validation

- All file paths are validated before processing
- PDF content is parsed through secure libraries (spaCy, Docling)
- No arbitrary code execution from PDF content

### Dependencies

- We use Dependabot for automated dependency updates
- Security vulnerabilities are monitored and addressed promptly
- All dependencies are pinned to specific versions

### Data Handling

- PDFs are processed in memory when possible
- Temporary files are cleaned up automatically
- No sensitive data is logged or stored

## Security Best Practices for Users

1. **Virtual Environment**: Always use a virtual environment
2. **Input Sources**: Only process PDFs from trusted sources
3. **File Permissions**: Limit access to processed data
4. **Updates**: Keep dependencies updated to latest secure versions

## Security Tools

We use the following tools to maintain security:

- **Bandit**: Python security linter for static analysis
- **Dependabot**: Automated dependency updates
- **CodeQL**: GitHub's semantic code analysis engine
- **Pre-commit hooks**: Automated code quality checks

## Responsible Disclosure

We follow responsible disclosure practices and coordinate with the security community. We ask that you:

- Give us reasonable time to fix issues before public disclosure
- Avoid accessing or modifying user data
- Respect the privacy and rights of other users

Thank you for helping keep our project and community secure!
