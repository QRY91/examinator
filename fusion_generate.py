#!/usr/bin/env python3
"""
EXAMINATOR FUSION GENERATE - Cloud-Local AI Orchestration
Democratizing AI-Assisted Education Through Constraint-Driven Innovation

Integrates existing Mistral workflow with Claude synthesis capabilities
Following 100r principles of intermittent connectivity and bandwidth consciousness
"""

import argparse
import sys
import json
import time
from pathlib import Path
from typing import List, Optional, Dict
from datetime import datetime

# Import existing examinator components
try:
    from generate import generate_flashcards_from_file, generate_wiki_from_file
    from fusion.fusion_core import FusionCore, FusionMode
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you're running from the examinator directory")
    sys.exit(1)

class FusionGenerator:
    """
    Orchestrates local and cloud AI for educational content generation
    
    Philosophy: Local-first with cloud augmentation during connectivity windows
    """
    
    def __init__(self):
        self.fusion = FusionCore()
        self.local_fallback = True
        
    def generate_content(
        self,
        files: List[str],
        content_type: str = "wiki",
        use_cloud: bool = False,
        priority: int = 5,
        local_fallback: bool = True
    ) -> Dict:
        """
        Generate educational content using optimal AI based on connectivity and preferences
        
        Args:
            files: Source files to process
            content_type: "wiki", "flashcards", or "comprehensive"
            use_cloud: Prefer cloud synthesis if available
            priority: 1-10 for cloud request prioritization
            local_fallback: Generate local content if cloud unavailable
        """
        
        results = {
            'strategy': 'unknown',
            'local_generated': [],
            'cloud_queued': [],
            'cloud_cached': [],
            'total_files': len(files)
        }
        
        if use_cloud:
            # Try cloud-first approach
            results.update(self._try_cloud_generation(files, content_type, priority))
            
            # Fallback to local if cloud unavailable and fallback enabled
            if local_fallback and not results['cloud_cached'] and not results['cloud_queued']:
                print("☁️ Cloud unavailable, falling back to local generation...")
                results.update(self._generate_local(files, content_type))
                results['strategy'] = 'cloud_attempted_local_fallback'
        else:
            # Local-first approach
            results.update(self._generate_local(files, content_type))
            results['strategy'] = 'local_primary'
            
        return results
    
    def _try_cloud_generation(self, files: List[str], content_type: str, priority: int) -> Dict:
        """Attempt cloud synthesis with intelligent caching"""
        results = {'cloud_queued': [], 'cloud_cached': []}
        
        for file_path in files:
            # Check if already cached
            request_id = f"{content_type}_{Path(file_path).stem}"
            cached_content = self.fusion.get_cached_knowledge(request_id)
            
            if cached_content:
                # Use cached cloud synthesis
                output_path = self._save_cached_content(file_path, cached_content, content_type)
                results['cloud_cached'].append({
                    'file': file_path,
                    'output': output_path,
                    'source': 'cloud_cache'
                })
                print(f"📚 Using cached cloud synthesis: {Path(file_path).name}")
            else:
                # Queue for next cloud sync
                queued_id = self.fusion.queue_synthesis_request(
                    source_files=[file_path],
                    request_type=f"{content_type}_synthesis",
                    parameters={'comprehensive': True, 'educational_focus': True},
                    priority=priority
                )
                results['cloud_queued'].append({
                    'file': file_path,
                    'request_id': queued_id,
                    'priority': priority
                })
                print(f"📝 Queued for cloud synthesis: {Path(file_path).name} (ID: {queued_id})")
        
        return results
    
    def _generate_local(self, files: List[str], content_type: str) -> Dict:
        """Generate content using local AI (Mistral)"""
        results = {'local_generated': []}
        
        for file_path in files:
            try:
                if content_type == "wiki":
                    output_path = generate_wiki_from_file(file_path)
                    source = 'local_wiki'
                elif content_type == "flashcards":
                    output_path = generate_flashcards_from_file(file_path)
                    source = 'local_flashcards'
                elif content_type == "comprehensive":
                    # Generate both
                    wiki_path = generate_wiki_from_file(file_path)
                    flash_path = generate_flashcards_from_file(file_path)
                    output_path = [wiki_path, flash_path]
                    source = 'local_comprehensive'
                else:
                    raise ValueError(f"Unknown content type: {content_type}")
                
                results['local_generated'].append({
                    'file': file_path,
                    'output': output_path,
                    'source': source
                })
                print(f"🤖 Generated locally: {Path(file_path).name}")
                
            except Exception as e:
                print(f"❌ Local generation failed for {file_path}: {e}")
                
        return results
    
    def _save_cached_content(self, source_file: str, content: str, content_type: str) -> str:
        """Save cached cloud content to appropriate output directory"""
        source_path = Path(source_file)
        
        if content_type == "wiki":
            output_dir = Path("wiki")
            suffix = "-cloud-wiki.md"
        else:
            output_dir = Path("flashcards")
            suffix = "-cloud-flashcards.md"
            
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"{source_path.stem}{suffix}"
        
        # Add metadata header
        timestamp = datetime.now().isoformat()
        header = f"""# {source_path.stem.title()} - Cloud Generated Content
*Generated via EXAMINATOR FUSION MODE*
*Source: {source_file}*
*Generated: {timestamp}*
*Model: Claude (cached)*

---

"""
        
        with open(output_path, 'w') as f:
            f.write(header + content)
            
        return str(output_path)
    
    def show_fusion_status(self):
        """Display comprehensive fusion mode status"""
        status = self.fusion.get_status()
        
        print("🤖 EXAMINATOR FUSION MODE STATUS")
        print("=" * 50)
        print(f"Operating Mode: {status['mode'].upper()}")
        print(f"Bandwidth Budget: {status['bandwidth_budget_mb']}MB")
        print()
        
        print("📝 CLOUD SYNTHESIS QUEUE:")
        if status['queue']['pending_requests'] > 0:
            print(f"  • {status['queue']['pending_requests']} requests pending")
            print(f"  • {status['queue']['total_estimated_tokens']} tokens estimated")
            print(f"  • {status['queue']['high_priority']} high priority")
        else:
            print("  • No requests queued")
        print()
        
        print("📚 KNOWLEDGE CACHE:")
        if status['cache']['total_entries'] > 0:
            print(f"  • {status['cache']['total_entries']} cached syntheses")
            print(f"  • {status['cache']['total_size_mb']}MB total size")
            if status['cache']['most_accessed']:
                print(f"  • Most used: {status['cache']['most_accessed']}")
        else:
            print("  • No cached knowledge")
        print()
        
        if status['last_uplink']:
            print(f"🌐 Last Cloud Sync: {status['last_uplink']}")
        else:
            print("🌐 No previous cloud sync recorded")
    
    def prepare_uplink_session(self, bandwidth_mb: float):
        """Prepare and display uplink session plan"""
        manifest = self.fusion.prepare_uplink_session(bandwidth_mb)
        
        print("🚀 FUSION UPLINK SESSION PREPARED")
        print("=" * 50)
        print(f"Bandwidth Budget: {manifest['budget_mb']}MB")
        print(f"Estimated Usage: {manifest['estimated_usage_mb']:.2f}MB")
        print(f"Selected Requests: {manifest['selected_requests']}")
        print(f"Total Queued: {manifest['total_queued']}")
        print()
        
        if manifest['requests']:
            print("📋 UPLINK MANIFEST:")
            for i, req in enumerate(manifest['requests'], 1):
                print(f"  {i}. {req['type']} (Priority: {req['priority']}, ~{req['tokens']} tokens)")
                for file in req['files']:
                    print(f"     📄 {Path(file).name}")
            print()
            print("💡 Ready for cloud synthesis! Run with --execute-uplink to proceed.")
        else:
            print("ℹ️ No requests fit within bandwidth budget")

def main():
    parser = argparse.ArgumentParser(
        description="🤖 EXAMINATOR FUSION MODE - Intelligent Cloud-Local AI Orchestration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
FUSION PHILOSOPHY:
  • Local-first: Always available, resource-conscious
  • Cloud-augmented: Deep synthesis during connectivity windows  
  • Bandwidth-conscious: Respect limited connectivity
  • Educational-focused: Build understanding, not dependency

EXAMPLES:
  # Generate with local fallback
  python3 fusion_generate.py --files *.cs --wiki --local-fallback
  
  # Queue for cloud synthesis
  python3 fusion_generate.py --files *.cs --wiki --cloud --priority 8
  
  # Comprehensive generation (wiki + flashcards)
  python3 fusion_generate.py --files *.cs --comprehensive --cloud
  
  # Check fusion status
  python3 fusion_generate.py --status
  
  # Prepare uplink session
  python3 fusion_generate.py --prepare-uplink 10.0
        """
    )
    
    # File specification
    parser.add_argument("--files", "-f", nargs="+", help="Source files to process")
    
    # Content type selection
    content_group = parser.add_mutually_exclusive_group()
    content_group.add_argument("--wiki", action="store_true", help="Generate wiki-style comprehensive summary")
    content_group.add_argument("--flashcards", action="store_true", help="Generate flashcard Q&A pairs")
    content_group.add_argument("--comprehensive", action="store_true", help="Generate both wiki and flashcards")
    
    # AI strategy selection
    strategy_group = parser.add_mutually_exclusive_group()
    strategy_group.add_argument("--cloud", action="store_true", help="Prefer cloud synthesis (queue if offline)")
    strategy_group.add_argument("--local", action="store_true", help="Use local AI only")
    
    # Cloud options
    parser.add_argument("--priority", type=int, default=5, choices=range(1, 11), 
                       help="Priority for cloud requests (1-10, higher = more urgent)")
    parser.add_argument("--no-fallback", action="store_true", 
                       help="Don't generate local content if cloud unavailable")
    
    # Fusion management
    parser.add_argument("--status", action="store_true", help="Show fusion mode status")
    parser.add_argument("--prepare-uplink", type=float, metavar="MB", 
                       help="Prepare uplink session with bandwidth budget (MB)")
    parser.add_argument("--cleanup", action="store_true", help="Clean up old cached content")
    
    args = parser.parse_args()
    
    fusion_gen = FusionGenerator()
    
    # Handle fusion management commands
    if args.status:
        fusion_gen.show_fusion_status()
        return
    
    if args.prepare_uplink:
        fusion_gen.prepare_uplink_session(args.prepare_uplink)
        return
        
    if args.cleanup:
        fusion_gen.fusion.cleanup_cache()
        print("🧹 Cache cleanup completed")
        return
    
    # Validate content generation arguments
    if not args.files:
        print("❌ No files specified. Use --files to specify source files.")
        parser.print_help()
        return
    
    # Determine content type
    if args.comprehensive:
        content_type = "comprehensive"
    elif args.flashcards:
        content_type = "flashcards"
    else:
        content_type = "wiki"  # Default
    
    # Determine strategy
    use_cloud = args.cloud or False
    local_fallback = not args.no_fallback
    
    print(f"🤖 EXAMINATOR FUSION MODE: {content_type.upper()} GENERATION")
    print(f"Strategy: {'Cloud-preferred' if use_cloud else 'Local-primary'}")
    print(f"Files: {len(args.files)}")
    print("=" * 50)
    
    # Generate content
    try:
        results = fusion_gen.generate_content(
            files=args.files,
            content_type=content_type,
            use_cloud=use_cloud,
            priority=args.priority,
            local_fallback=local_fallback
        )
        
        # Report results
        print()
        print("📊 GENERATION RESULTS:")
        print(f"Strategy Used: {results['strategy']}")
        print(f"Local Generated: {len(results['local_generated'])}")
        print(f"Cloud Cached: {len(results['cloud_cached'])}")
        print(f"Cloud Queued: {len(results['cloud_queued'])}")
        
        if results['cloud_queued']:
            print()
            print("💡 Cloud requests queued! Use --prepare-uplink to plan synthesis session.")
            
    except KeyboardInterrupt:
        print("\n🛑 Generation interrupted by user")
    except Exception as e:
        print(f"❌ Generation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()