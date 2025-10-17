# Pull Request Template

## Description
<!--- Describe your changes in detail -->

## Type of Change
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] 🐛 **Bug fix** (non-breaking change which fixes an issue)
- [ ] ✨ **New feature** (non-breaking change which adds functionality)
- [ ] 💥 **Breaking change** (fix or feature that would cause existing functionality to change)
- [ ] 🏗️ **Code refactor** (no functional changes)
- [ ] 📚 **Documentation update**
- [ ] 🧪 **Tests** (adding missing tests or correcting existing tests)
- [ ] 🔧 **Maintenance** (dependency updates, tooling, etc.)
- [ ] 🎨 **Style** (code formatting, style updates)
- [ ] ⚡ **Performance** (improvements to speed or memory usage)
- [ ] 🔒 **Security** (fixes or improvements to security)

## Changes Made
<!--- List the specific changes you made -->

### Files Changed
<!--- List the files you've modified -->

### Key Changes
<!--- Describe the most important changes in detail -->

## Testing
<!--- Please describe the tests that you ran to verify your changes -->

### Test Results
<!--- Include test output or describe test coverage -->

- [ ] ✅ All existing tests pass
- [ ] ✅ New tests added (if applicable)
- [ ] ✅ Test coverage maintained/improved
- [ ] ✅ Manual testing performed

### Test Commands Run

```bash
# Example test commands
pytest --cov --cov-branch --cov-report=xml --junitxml=junit.xml -o junit_family=legacy
pytest --cov-report=html
```

## Code Quality
<!--- Ensure your code follows the project's standards -->

- [ ] ✅ Code follows PEP 8 style guidelines
- [ ] ✅ Black formatting applied
- [ ] ✅ Flake8 linting passes
- [ ] ✅ Bandit security scan passes
- [ ] ✅ Type hints added/updated (where applicable)
- [ ] ✅ Docstrings added/updated (where applicable)

## Documentation Updates
<!--- Update documentation as needed -->

- [ ] ✅ README.md updated (if applicable)
- [ ] ✅ Docstrings updated
- [ ] ✅ Comments added for complex logic
- [ ] ✅ API documentation updated (if applicable)

## CI/CD Status
<!--- Check CI/CD pipeline results -->

- [ ] ✅ GitHub Actions CI passes
- [ ] ✅ Codecov coverage meets requirements (≥80%)
- [ ] ✅ Security scans pass
- [ ] ✅ All quality checks pass

## Breaking Changes
<!--- If this PR contains breaking changes, please describe them -->

**Does this PR introduce breaking changes?**

- [ ] No
- [ ] Yes (please describe below)

**Breaking Changes Description:**
<!--- Describe any breaking changes and migration instructions -->

## Related Issues
<!--- Link to any related issues this PR addresses -->

Closes #<!-- issue number -->
Related to #<!-- issue number -->

## Screenshots/Visual Changes
<!--- If applicable, add screenshots or describe visual changes -->

## Additional Context
<!--- Add any other context about the PR here -->

## Checklist
<!--- Go over all the following points, and put an `x` in all the boxes that apply -->

### General

- [ ] ✅ PR title follows conventional commit format (e.g., `feat: add new feature`)
- [ ] ✅ PR description is clear and comprehensive
- [ ] ✅ Self-reviewed the code changes
- [ ] ✅ Code follows project conventions

### Testing & Quality

- [ ] ✅ Tests written for new functionality
- [ ] ✅ Tests pass locally and in CI
- [ ] ✅ Code coverage maintained or improved
- [ ] ✅ No new linting errors introduced
- [ ] ✅ No new security vulnerabilities introduced

### Documentation

- [ ] ✅ Documentation updated for any new features
- [ ] ✅ README.md updated if needed
- [ ] ✅ Comments added for complex code sections

### Dependencies

- [ ] ✅ No unnecessary dependencies added
- [ ] ✅ Dependencies are pinned to specific versions
- [ ] ✅ Security vulnerabilities checked for new dependencies

### Performance & Security

- [ ] ✅ No performance regressions introduced
- [ ] ✅ Security best practices followed
- [ ] ✅ No sensitive data exposed

## Reviewers
<!--- Request reviews from specific team members if needed -->
<!-- @username -->

## Deployment Notes
<!--- Any special deployment considerations -->

**Ready for review and merge?**

- [ ] ✅ Yes, this PR is ready for review
- [ ] 🔄 No, this PR needs more work

---

*By submitting this pull request, I confirm that my contribution is made under the terms of the GPL-3.0 license.*
