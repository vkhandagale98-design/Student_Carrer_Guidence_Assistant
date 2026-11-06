
from career_engine import generate_rule_based_plan, load_knowledge

def test_knowledge_base_has_roles_and_resources():
    data = load_knowledge()
    assert len(data["roles"]) >= 3
    assert len(data["learning_resources"]) >= 3
    assert len(data["job_search_resources"]) >= 3

def test_rule_based_plan_returns_three_roles():
    profile = {
        "qualification": "Undergraduate",
        "department": "Computer Science",
        "degree": "B.Tech",
        "year": "Final year",
        "skills": ["Python", "SQL"],
        "interests": ["artificial intelligence", "machine learning"],
        "industry": "Information Technology",
        "goal": "Become an AI engineer",
        "location": "India",
    }
    plan = generate_rule_based_plan(profile)
    assert len(plan["career_paths"]) == 3
    assert "skill_gap" in plan
    assert len(plan["roadmap"]) == 3
    assert plan["learning_resources"]
    assert plan["job_search_resources"]
