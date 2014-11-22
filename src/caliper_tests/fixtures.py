# -*- coding: utf-8 -*-
# Caliper-python testing package (packet body fixtures)
#
# Copyright (c) 2014 IMS Global Learning Consortium, Inc. All Rights Reserved.
# Trademark Information- http://www.imsglobal.org/copyright.html

# IMS Global Caliper Analytics™ APIs are publicly licensed as Open Source
# Software via GNU General Public License version 3.0 GPL v3. This license
# contains terms incompatible with use in closed-source software including a
# copyleft provision.

# IMS Global also makes available an Alternative License based on the GNU Lesser
# General Public License. LGPL v3 Licensees (via the Alternative License) are
# required to be IMS Global members. Membership in IMS is a commitment by a
# supplier to the IMS community for ongoing support for achieving "plug and play"
# integration.  IMS Membership dues pay for ongoing maintenance for the
# Alternative License to be applicable to updates to the Caliper Analytics
# APIs. The rationale for this dual-license approach and membership component is
# to help assure a requisite level of ongoing development, project management,
# and support for the software.

# Licensees of IMS Global Caliper Analytics APIs are strongly encouraged to
# become active contributors to the Caliper Analytics project and other projects
# within IMS Global. Prospective licensees should understand that their initial
# base contribution and ongoing membership fees are insufficient to fully fund
# the ongoing development and maintenance of Caliper APIs and that voluntary
# contributions are the primary "fuel" ensuring any open source project's
# viability. Contributions can include development, bug fixing, bug reporting,
# performance analysis, and other aspects of the overall development process.

# Contributor status at the "github" level will be individual-based. Contributors
# will need to sign an IMS Global Contributor License Agreement (CLA) that grants
# IMS Global a license to contributions.

# If you are interested in licensing the IMS Global Caliper Analytics APIs please
# email licenses@imsglobal.org



EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/NavigationEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/NavigationEvent",
    "actor": {
        "@id": "uri:/someEdu/user/42",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "lastModifiedTime": 0,
        "properties": {}
    },
    "action": "navigated to",
    "object": {
        "@id": "uri:/someEdu/reading/42",
        "@type": "http://purl.imsglobal.org/caliper/v1/ActivityContext",
        "name": null,
        "lastModifiedTime": 0,
        "properties": {}
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
        "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
        "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": null,
        "lastModifiedTime": 1402965614516
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": null,
    "group": null,
    "navigatedFrom": {
        "@id": "AmRev-101-landingPage",
        "@type": "http://purl.imsglobal.org/caliper/v1/WebPage",
        "name": "American Revolution 101 Landing Page",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": null,
        "lastModifiedTime": 0
    }
}'''

ASSESSMENT_EVENT='''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AssessmentEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "started",
    "object": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
        "@type": "http://purl.imsglobal.org/caliper/v1/Assessment",
        "name": "American Revolution - Key Figures Assessment",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "lastModifiedTime": 1402965614516,
        "dateCreated": 1402965614516,
        "datePublished": 1402965614516,
        "dateToActivate": 1402965614516,
        "dateToShow": 1402965614516,
        "dateToStartOn": 1402965614516,
        "dateToSubmit": 1402965614516,
        "maxAttempts": 2,
        "maxSubmits": 2,
        "maxScore": 3.0,
        "assessmentItems": [
            { "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item1",
                "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
                "name": "Assessment Item 1",
                "objectType": [],
                "properties": {},
                "alignedLearningObjective": [],
                "keyword": [],
                "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
                "lastModifiedTime": 0,
                "dateCreated": 0,
                "datePublished": 0,
                "dateToActivate": 0,
                "dateToShow": 0,
                "dateToStartOn": 0,
                "dateToSubmit": 0,
                "maxAttempts": 2,
                "maxSubmits": 2,
                "maxScore": 1.0 },
            { "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item2",
                "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
                "name": "Assessment Item 2",
                "objectType": [],
                "properties": {},
                "alignedLearningObjective": [],
                "keyword": [],
                "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
                "lastModifiedTime": 0,
                "dateCreated": 0,
                "datePublished": 0,
                "dateToActivate": 0,
                "dateToShow": 0,
                "dateToStartOn": 0,
                "dateToSubmit": 0,
                "maxAttempts": 2,
                "maxSubmits": 2,
                "maxScore": 1.0 },
            { "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item3",
                "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
                "name": "Assessment Item 3",
                "objectType": [],
                "properties": {},
                "alignedLearningObjective": [],
                "keyword": [],
                "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
                "lastModifiedTime": 0,
                "dateCreated": 0,
                "datePublished": 0,
                "dateToActivate": 0,
                "dateToShow": 0,
                "dateToStartOn": 0,
                "dateToSubmit": 0,
                "maxAttempts": 2,
                "maxSubmits": 2,
                "maxScore": 1.0 }]
    },
    "target": null,
    "generated": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/attempt1",
        "@type": "http://purl.imsglobal.org/caliper/v1/Attempt",
        "name": null,
        "properties": {},
        "lastModifiedTime": 0,
        "count": 1,
        "startedAtTime": 0,
        "endedAtTime": 0,
        "duration": null
    },
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

ASSESSMENT_ITEM_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AssessmentItemEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItemEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "started",
    "object": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item1",
        "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
        "name": "Assessment Item 1",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
        "lastModifiedTime": 0,
        "dateCreated": 0,
        "datePublished": 0,
        "dateToActivate": 0,
        "dateToShow": 0,
        "dateToStartOn": 0,
        "dateToSubmit": 0,
        "maxAttempts": 2,
        "maxSubmits": 2,
        "maxScore": 1.0 },
    "target": null,
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

ASSESSMENT_OUTCOME_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/OutcomeEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/OutcomeEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "graded",
    "object": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/attempt1",
        "@type": "http://purl.imsglobal.org/caliper/v1/Attempt",
        "name": null,
        "properties": {},
        "lastModifiedTime": 0,
        "count": 1,
        "startedAtTime": 0,
        "endedAtTime": 0,
        "duration": null
    },
    "target": null,
    "generated": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/attempt1/result",
        "@type": "http://purl.imsglobal.org/caliper/v1/Result",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516,
        "normalScore": 3.0,
        "penaltyScore": 0.0,
        "extraCreditScore": 0.0,
        "totalScore": 3.0,
        "curvedTotalScore": 3.0,
        "curveFactor": 0.0,
        "comment":"Well done.",
        "scoredBy": null
    },
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

ASSIGNABLE_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AssignableEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AssignableEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "started",
    "object": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
        "@type": "http://purl.imsglobal.org/caliper/v1/Assessment",
        "name": "American Revolution - Key Figures Assessment",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "lastModifiedTime": 1402965614516,
        "dateCreated": 1402965614516,
        "datePublished": 1402965614516,
        "dateToActivate": 1402965614516,
        "dateToShow": 1402965614516,
        "dateToStartOn": 1402965614516,
        "dateToSubmit": 1402965614516,
        "maxAttempts": 2,
        "maxSubmits": 2,
        "maxScore": 3.0,
        "assessmentItems": [
            { "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item1",
            "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
            "name": "Assessment Item 1",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
            "lastModifiedTime": 0,
            "dateCreated": 0,
            "datePublished": 0,
            "dateToActivate": 0,
            "dateToShow": 0,
            "dateToStartOn": 0,
            "dateToSubmit": 0,
            "maxAttempts": 2,
            "maxSubmits": 2,
            "maxScore": 1.0 },
            { "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item2",
            "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
            "name": "Assessment Item 2",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
            "lastModifiedTime": 0,
            "dateCreated": 0,
            "datePublished": 0,
            "dateToActivate": 0,
            "dateToShow": 0,
            "dateToStartOn": 0,
            "dateToSubmit": 0,
            "maxAttempts": 2,
            "maxSubmits": 2,
            "maxScore": 1.0 },
            { "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/item3",
            "@type": "http://purl.imsglobal.org/caliper/v1/AssessmentItem",
            "name": "Assessment Item 3",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1",
            "lastModifiedTime": 0,
            "dateCreated": 0,
            "datePublished": 0,
            "dateToActivate": 0,
            "dateToShow": 0,
            "dateToStartOn": 0,
            "dateToSubmit": 0,
            "maxAttempts": 2,
            "maxSubmits": 2,
            "maxScore": 1.0 }]
    },
    "target": null,
    "generated": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101/assessment1/attempt1",
        "@type": "http://purl.imsglobal.org/caliper/v1/Attempt",
        "name": null,
        "properties": {},
        "lastModifiedTime": 0,
        "count": 1,
        "startedAtTime": 0,
        "endedAtTime": 0,
        "duration": null
    },
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

BOOKMARK_ANNOTATION_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AnnotationEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AnnotationEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "bookmarked",
    "object": {
        "@id": "https://someEduApp.edu/bookmarks/00001",
        "@type": "http://purl.imsglobal.org/caliper/v1/BookmarkAnnotation",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516,
        "bookmarkNotes": "The Intolerable Acts (1774)--bad idea Lord North"
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/2)",
        "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
        "name": "Key Figures: Lord North",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516,
        "index": 2
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

HIGHLIGHT_ANNOTATION_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AnnotationEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AnnotationEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "highlighted",
    "object": {
        "@id": "https://someEduApp.edu/highlights/12345",
        "@type": "http://purl.imsglobal.org/caliper/v1/HighlightAnnotation",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516,
        "selection": {
            "start": "455",
            "end": "489"
        },
        "selectionText": "Life, Liberty and the pursuit of Happiness"
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)",
        "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
        "name": "Key Figures: George Washington",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516,
        "index": 1
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

MEDIA_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/MediaEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/MediaEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "paused",
    "object": {
        "@id": "https://com.sat/super-media-tool/video/video1",
        "@type": "http://purl.imsglobal.org/caliper/v1/VideoObject",
        "name": "American Revolution - Key Figures Video",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [{
            "@id": "http://americanrevolution.com/personalities/learn",
            "@type": "http://purl.imsglobal.org/caliper/v1/LearningObjective",
            "name": null,
            "properties": {},
            "lastModifiedTime": 0
        }],
        "keyword": [],
        "partOf": null,
        "lastModifiedTime": 1402965614516,
        "duration": 1420
    },
    "mediaLocation": {
        "@id": "https://com.sat/super-media-tool/video/video1",
        "@type": "http://purl.imsglobal.org/caliper/v1/MediaLocation",
        "name": null,
        "properties": {},
        "lastModifiedTime": 0,
        "currentTime": 710
    },
    "target": null,
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

NAVIGATION_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/NavigationEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/NavigationEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "navigated to",
    "object": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
        "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
        "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": null,
        "lastModifiedTime": 1402965614516
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)",
        "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
        "name": "Key Figures: George Washington",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516,
        "index": 1
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "navigatedFrom": {
        "@id": "AmRev-101-landingPage",
        "@type": "http://purl.imsglobal.org/caliper/v1/WebPage",
        "name": "American Revolution 101 Landing Page",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
            "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
            "semester": "Spring-2014",
            "courseNumber": "AmRev-101",
            "label": "Am Rev 101",
            "name": "American Revolution 101",
            "parentOrg": null,
            "properties": {},
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516
    }
}'''

SHARED_ANNOTATION_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AnnotationEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AnnotationEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "shared",
    "object": {
        "@id": "https://someEduApp.edu/shared/9999",
        "@type": "http://purl.imsglobal.org/caliper/v1/SharedAnnotation",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516,
        "withAgents": [
            {"@id": "https://some-university.edu/students/657585",
            "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
            "name": null,
            "properties": {},
            "lastModifiedTime": 1402965614516},
            {"@id": "https://some-university.edu/students/667788",
            "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
            "name": null,
            "properties": {},
            "lastModifiedTime": 1402965614516}]
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/3)",
        "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
        "name": "Key Figures: John Adams",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516,
        "index": 3
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

TAG_ANNOTATION_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/AnnotationEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/AnnotationEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "shared",
    "object": {
        "@id": "https://someEduApp.edu/tags/7654",
        "@type": "http://purl.imsglobal.org/caliper/v1/TagAnnotation",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516,
        "tags": ["to-read", "1765", "shared-with-project-team"]
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/4)",
        "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
        "name": "The Stamp Act Crisis",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516,
        "index": 4
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

VIEW_EVENT = '''{
    "@context": "http://purl.imsglobal.org/ctx/caliper/v1/ViewEvent",
    "@type": "http://purl.imsglobal.org/caliper/v1/ViewEvent",
    "actor": {
        "@id": "https://some-university.edu/user/554433",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
        "name": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "action": "viewed",
    "object": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
        "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
        "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": null,
        "lastModifiedTime": 1402965614516
    },
    "target": {
        "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)",
        "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
        "name": "Key Figures: George Washington",
        "objectType": [],
        "properties": {},
        "alignedLearningObjective": [],
        "keyword": [],
        "partOf": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "lastModifiedTime": 1402965614516,
        "index": 1
    },
    "generated": null,
    "startedAtTime": 1402965614516,
    "endedAtTime": 0,
    "duration": null,
    "edApp": {
        "@id": "https://github.com/readium/readium-js-viewer",
        "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
        "name": "Readium",
        "properties": {},
        "lastModifiedTime": 1402965614516
    },
    "group": {
        "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
        "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
        "semester": "Spring-2014",
        "courseNumber": "AmRev-101",
        "label": "Am Rev 101",
        "name": "American Revolution 101",
        "parentOrg": null,
        "properties": {},
        "lastModifiedTime": 1402965614516
    }
}'''

EVENT_STORE_PAYLOAD = '''[{
    "id"  : "caliper-java_fccffd9b-68d5-4183-b563-e22136aafaa3",
    "type": "caliperEvent",
    "time": "2014-07-01T14:29:29.858-04:00",
    "data": {
        "@context": "http://purl.imsglobal.org/ctx/caliper/v1/NavigationEvent",
        "@type": "http://purl.imsglobal.org/caliper/v1/NavigationEvent",
        "actor": {
            "@id": "https://some-university.edu/user/554433",
            "@type": "http://purl.imsglobal.org/caliper/v1/lis/Person",
            "name": null,
            "properties": {},
            "lastModifiedTime": 1402965614516
        },
        "action": "navigated to",
        "object": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
            "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
            "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": null,
            "lastModifiedTime": 1402965614516
        },
        "target": {
            "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3/1)",
            "@type": "http://purl.imsglobal.org/caliper/v1/Frame",
            "name": "Key Figures: George Washington",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": {
                "@id": "https://github.com/readium/readium-js-viewer/book/34843#epubcfi(/4/3)",
                "@type": "http://www.idpf.org/epub/vocab/structure/#volume",
                "name": "The Glorious Cause: The American Revolution, 1763-1789 (Oxford History of the United States)",
                "objectType": [],
                "properties": {},
                "alignedLearningObjective": [],
                "keyword": [],
                "partOf": null,
                "lastModifiedTime": 1402965614516
            },
            "lastModifiedTime": 1402965614516,
            "index": 1
        },
        "generated": null,
        "startedAtTime": 1402965614516,
        "endedAtTime": 0,
        "duration": null,
        "edApp": {
            "@id": "https://github.com/readium/readium-js-viewer",
            "@type":"http://purl.imsglobal.org/caliper/v1/SoftwareApplication",
            "name": "Readium",
            "properties": {},
            "lastModifiedTime": 1402965614516
        },
        "group": {
            "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
            "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
            "semester": "Spring-2014",
            "courseNumber": "AmRev-101",
            "label": "Am Rev 101",
            "name": "American Revolution 101",
            "parentOrg": null,
            "properties": {},
            "lastModifiedTime": 1402965614516
        },
        "navigatedFrom": {
            "@id": "AmRev-101-landingPage",
            "@type": "http://purl.imsglobal.org/caliper/v1/WebPage",
            "name": "American Revolution 101 Landing Page",
            "objectType": [],
            "properties": {},
            "alignedLearningObjective": [],
            "keyword": [],
            "partOf": {
                "@id": "https://some-university.edu/politicalScience/2014/american-revolution-101",
                "@type": "http://purl.imsglobal.org/caliper/v1/lis/CourseSection",
                "semester": "Spring-2014",
                "courseNumber": "AmRev-101",
                "label": "Am Rev 101",
                "name": "American Revolution 101",
                "parentOrg": null,
                "properties": {},
                "lastModifiedTime": 1402965614516
            },
            "lastModifiedTime": 1402965614516
        }
    }
}]'''
