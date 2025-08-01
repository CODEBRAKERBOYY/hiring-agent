from typing import List, Optional, Dict, Tuple
from pydantic import BaseModel, Field, field_validator

class Location(BaseModel):
    """Location information for JSON Resume format."""
    address: Optional[str] = None
    postalCode: Optional[str] = None
    city: Optional[str] = None
    countryCode: Optional[str] = None
    region: Optional[str] = None

class Profile(BaseModel):
    """Social profile information for JSON Resume format."""
    network: Optional[str] = None
    username: Optional[str] = None
    url: str

class Basics(BaseModel):
    """Basic information for JSON Resume format."""
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    url: Optional[str] = None
    summary: Optional[str] = None
    location: Optional[Location] = None
    profiles: Optional[List[Profile]] = None

class Work(BaseModel):
    """Work experience for JSON Resume format."""
    name: Optional[str] = None
    position: Optional[str] = None
    url: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    summary: Optional[str] = None
    highlights: Optional[List[str]] = None

class Volunteer(BaseModel):
    """Volunteer experience for JSON Resume format."""
    organization: Optional[str] = None
    position: Optional[str] = None
    url: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    summary: Optional[str] = None
    highlights: Optional[List[str]] = None

class Education(BaseModel):
    """Education information for JSON Resume format."""
    institution: Optional[str] = None
    url: Optional[str] = None
    area: Optional[str] = None
    studyType: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    score: Optional[str] = None
    courses: Optional[List[str]] = None

class Award(BaseModel):
    """Award information for JSON Resume format."""
    title: Optional[str] = None
    date: Optional[str] = None
    awarder: Optional[str] = None
    summary: Optional[str] = None

class Certificate(BaseModel):
    """Certificate information for JSON Resume format."""
    name: Optional[str] = None
    date: Optional[str] = None
    issuer: Optional[str] = None
    url: Optional[str] = None

class Publication(BaseModel):
    """Publication information for JSON Resume format."""
    name: Optional[str] = None
    publisher: Optional[str] = None
    releaseDate: Optional[str] = None
    url: Optional[str] = None
    summary: Optional[str] = None

class Skill(BaseModel):
    """Skill information for JSON Resume format."""
    name: Optional[str] = None
    level: Optional[str] = None
    keywords: Optional[List[str]] = None

class Language(BaseModel):
    """Language information for JSON Resume format."""
    language: Optional[str] = None
    fluency: Optional[str] = None

class Interest(BaseModel):
    """Interest information for JSON Resume format."""
    name: Optional[str] = None
    keywords: Optional[List[str]] = None

class Reference(BaseModel):
    """Reference information for JSON Resume format."""
    name: Optional[str] = None
    reference: Optional[str] = None

class Project(BaseModel):
    """Project information for JSON Resume format."""
    name: Optional[str] = None
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    description: Optional[str] = None
    highlights: Optional[List[str]] = None
    url: Optional[str] = None
    technologies: Optional[List[str]] = None
    skills: Optional[List[str]] = None

class BasicsSection(BaseModel):
    """Basics section containing basic information."""
    basics: Optional[Basics] = None

class WorkSection(BaseModel):
    """Work section containing a list of work experiences."""
    work: Optional[List[Work]] = None

class EducationSection(BaseModel):
    """Education section containing a list of education entries."""
    education: Optional[List[Education]] = None

class SkillsSection(BaseModel):
    """Skills section containing a list of skill categories."""
    skills: Optional[List[Skill]] = None

class ProjectsSection(BaseModel):
    """Projects section containing a list of projects."""
    projects: Optional[List[Project]] = None

class AwardsSection(BaseModel):
    """Awards section containing a list of awards."""
    awards: Optional[List[Award]] = None
    
class JSONResume(BaseModel):
    """Complete JSON Resume format model."""
    basics: Optional[Basics] = None
    work: Optional[List[Work]] = None
    volunteer: Optional[List[Volunteer]] = None
    education: Optional[List[Education]] = None
    awards: Optional[List[Award]] = None
    certificates: Optional[List[Certificate]] = None
    publications: Optional[List[Publication]] = None
    skills: Optional[List[Skill]] = None
    languages: Optional[List[Language]] = None
    interests: Optional[List[Interest]] = None
    references: Optional[List[Reference]] = None
    projects: Optional[List[Project]] = None

class CategoryScore(BaseModel):
    score: float = Field(ge=0, description="Score achieved in this category")
    max: int = Field(gt=0, description="Maximum possible score")
    evidence: str = Field(min_length=1, description="Evidence supporting the score")

class Scores(BaseModel):
    open_source: CategoryScore
    self_projects: CategoryScore
    production: CategoryScore
    technical_skills: CategoryScore

class BonusPoints(BaseModel):
    total: float = Field(ge=0, le=20, description="Total bonus points")
    breakdown: str = Field(description="Breakdown of bonus points")

class Deductions(BaseModel):
    total: float = Field(ge=0, description="Total deduction points (stored as positive, applied as negative)")
    reasons: str = Field(description="Reasons for deductions")

class EvaluationData(BaseModel):
    scores: Scores
    bonus_points: BonusPoints
    deductions: Deductions
    key_strengths: List[str] = Field(min_items=1, max_items=5)
    areas_for_improvement: List[str] = Field(min_items=1, max_items=3)

class GitHubProfile(BaseModel):
    """Pydantic model for GitHub profile data."""
    username: str
    name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    company: Optional[str] = None
    public_repos: Optional[int] = None
    followers: Optional[int] = None
    following: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    avatar_url: Optional[str] = None
    blog: Optional[str] = None
    twitter_username: Optional[str] = None
    hireable: Optional[bool] = None